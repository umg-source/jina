from jina.executors.encoders.nlp.farm import FarmTextEncoder
from tests.unit.executors.encoders.nlp import NlpTestCase


class FarmTestCase(NlpTestCase):
    def _get_encoder(self, metas):
        return FarmTextEncoder(metas=metas)
