from nomad.config.models.plugins import NormalizerEntryPoint
from pydantic import Field


class MyNormalizerEntryPoint(NormalizerEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_dls_measurements.normalizers.mynormalizer import MyNormalizer

        return MyNormalizer(**self.dict())


mynormalizer = MyNormalizerEntryPoint(
    name='MyNormalizer',
    description='Normalizer defined using the new plugin mechanism.',
)
