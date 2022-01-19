from django.core.exceptions import ValidationError
from django.db import models

from economy_sector_module.utils import STANDARDS, get_or_none


class EconomySector(models.Model):
    standard = models.IntegerField(choices=STANDARDS, default=STANDARDS.unspecified,
                                   help_text="The standard this code is defined by.")
    level = models.PositiveSmallIntegerField()
    label = models.CharField(max_length=256)
    code = models.CharField(max_length=16, help_text="Code as defined by a standard.")
    parent = models.ForeignKey(to='self', related_name='children', null=True,
                               on_delete=models.CASCADE)
    top_parent = models.ForeignKey(to='self', related_name='bottom_children', null=True,
                                   on_delete=models.CASCADE)

    class Meta:
        unique_together = [('standard', 'code')]

    def get_corresponding_relation(self, standard):
        """
        Find the corresponding economy sector of a given standard.

        Args:
            standard: The standard with which we search the corresponding sector.
        """
        return get_or_none(
            EconomySectorRelation.objects,
            from_sector=self,
            to_standard=standard
        )

    def save(self, *args, **kwargs, ):
        raise ValidationError("You can not create new economy sectors! Please use the prepared data!")

    def __str__(self):
        return f'{self.label}-{self.code}'


class EconomySectorRelation(models.Model):
    from_sector = models.ForeignKey(to='EconomySector', on_delete=models.CASCADE,
                                    related_name='from_relations',
                                    help_text="The economy sector we want to convert.")
    to_standard = models.IntegerField(choices=STANDARDS, default=STANDARDS.unspecified,
                                      help_text="The standard in which the conversion is happening.")
    to_sector = models.ForeignKey(to='EconomySector', on_delete=models.CASCADE,
                                  related_name='to_relations',
                                  help_text="The corresponding sector in the given standard.")

    class Meta:
        unique_together = ('from_sector', 'to_standard', 'to_sector')

    def __str__(self):
        return f'{self.from_sector.code}-{self.to_sector.code}'

