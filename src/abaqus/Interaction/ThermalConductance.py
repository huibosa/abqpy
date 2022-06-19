from abaqusConstants import *


class ThermalConductance:
    """The ThermalConductance object specifies thermal conductance for a contact interaction
    property.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactionProperties[name].thermalConductance

        The table data for this object are:
        The **clearanceDepTable** data specify the following:
            - Conductivity.
            - Clearance.
            - Temperature, if the data depend on temperature.
            - Mass flow rate, if the data depend on mass flow rate.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        The **pressureDepTable** data specify the following:
            - Conductivity.
            - Pressure.
            - Temperature, if the data depend on temperature.
            - Mass flow rate, if the data depend on mass flow rate.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

    The corresponding analysis keywords are:

    - GAP CONDUCTANCE
    """

    def __init__(
        self,
        definition: SymbolicConstant = TABULAR,
        clearanceDependency: Boolean = ON,
        pressureDependency: Boolean = OFF,
        temperatureDependencyC: Boolean = OFF,
        massFlowRateDependencyC: Boolean = OFF,
        dependenciesC: int = 0,
        clearanceDepTable: tuple = (),
        temperatureDependencyP: Boolean = OFF,
        massFlowRateDependencyP: Boolean = OFF,
        dependenciesP: int = 0,
        pressureDepTable: tuple = (),
    ):
        """This method creates a ThermalConductance object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].interactionProperties[name].ThermalConductance

        Parameters
        ----------
        definition
            A SymbolicConstant specifying how the thermal conductance is defined. Possible values
            are TABULAR and USER_DEFINED. The default value is TABULAR.
        clearanceDependency
            A Boolean specifying whether to use clearance-dependent data. The default value is ON.
        pressureDependency
            A Boolean specifying whether to use pressure-dependent data. The default value is OFF.
        temperatureDependencyC
            A Boolean specifying whether to use temperature-dependent data with clearance
            dependency. The default value is OFF.
        massFlowRateDependencyC
            A Boolean specifying whether to use mass-flow-rate-dependent data with clearance
            dependency. The default value is OFF.
        dependenciesC
            An Int specifying the number of field variables to use with clearance dependency. The
            default value is 0.
        clearanceDepTable
            A sequence of sequences of Floats specifying clearance dependency data. The items in the
            table data are described below.
        temperatureDependencyP
            A Boolean specifying whether to use temperature-dependent data with pressure dependency.
            The default value is OFF.
        massFlowRateDependencyP
            A Boolean specifying whether to use mass-flow-rate-dependent data with pressure
            dependency. The default value is OFF.
        dependenciesP
            An Int specifying the number of field variables to use with pressure dependency. The
            default value is 0.
        pressureDepTable
            A sequence of sequences of Floats specifying pressure dependency data. The items in the
            table data are described below.

        Returns
        -------
            A ThermalConductance object.
        """
        pass

    def setValues(self):
        """This method modifies the ThermalConductance object."""
        pass
