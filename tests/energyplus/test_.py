import pytest

class Test_:
    def test_(self):
        import energyplus as pyenergyplus
        pyenergyplus.api.EnergyPlusAPI.api_version()

        api = pyenergyplus.api.EnergyPlusAPI()
        api.runtime.run_energyplus(
            api.state_manager.new_state(), 
            ['--help']
        )
        assert api.runtime.run_energyplus(
            api.state_manager.new_state(), 
            ['--version']
        ) == 0
