from abaqusConstants import *


class CastIronCompressionHardening:
    r"""The CastIronCompressionHardening object specifies hardening for the Cast- Iron
    plasticity model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].castIronPlasticity.castIronCompressionHardening
        import odbMaterial
        session.odbs[name].materials[name].castIronPlasticity.castIronCompressionHardening

    The table data for this object are:

    - Yield stress in compression, :math:`\sigma_c`.
    - The absolute value of the corresponding Plastic strain.(The first tabular value entered must always be zero.)
    - Temperature, if the data depend on temperature.
    - Value of the first field variable, if the data depend on field variables.
    - Value of the second field variable.
    - Etc.

    The corresponding analysis keywords are:

    - CAST IRON COMPRESSION HARDENING
    """

    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a CastIronCompressionHardening object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].castIronPlasticity.CastIronCompressionHardening.CastIronCompressionHardenings[name].castIronPlasticity.CastIronCompressionHardening
        
        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
        CastIronCompressionHardening
            A :py:class:`~abaqus.Material.Plastic.Metal.CastIron.CastIronCompressionHardening.CastIronCompressionHardening` object. 

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the CastIronCompressionHardening object.

        Raises
        ------
        RangeError
        """
        pass
