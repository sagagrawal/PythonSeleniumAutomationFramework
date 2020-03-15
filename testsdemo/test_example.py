from utilities.Base import Base


class TestExample(Base):
    def test_ex1(self):
        self.log.debug("THis is a debug message print")
        assert 5 == 5

