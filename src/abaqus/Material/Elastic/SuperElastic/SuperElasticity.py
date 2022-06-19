from ...Plastic.SuperElastic.SuperElasticHardening import SuperElasticHardening
from ...Plastic.SuperElastic.SuperElasticHardeningModifications import (
    SuperElasticHardeningModifications,
)


class SuperElasticity:
    """The SuperElasticity object specifies a superelastic material model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].superElasticity
        import odbMaterial
        session.odbs[name].materials[name].superElasticity

    The table data for this object are:
        - Young's Modulus (Martensite).
        - Poisson's Ratio (Martensite).
        - Transformation Strain.
        - Start of Transformation (Loading).
        - End of Transformation (Loading).
        - Start of Transformation (Unloading).
        - End of Transformation (Unloading).
        - Start of Transformation in Compression (Loading).
        - Reference Temperature.
        - Loading.
        - Unloading.

    The corresponding analysis keywords are:

    - SUPERELASTIC
    """

    # A [SuperElasticHardening
    # object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningpyc.htm?ContextScope=all#simaker-c-superelastichardeningpyc).
    superElasticHardening: SuperElasticHardening = SuperElasticHardening(((),))

    # A [SuperElasticHardeningModifications
    # object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-superelastichardeningmodificationpyc.htm?ContextScope=all#simaker-c-superelastichardeningmodificationpyc).
    superElasticHardeningModifications: SuperElasticHardeningModifications = (
        SuperElasticHardeningModifications(((),))
    )

    def __init__(self, table: tuple, nonassociated: float = None):
        """This method creates a SuperElasticity object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].materials[name].SuperElasticity
            session.odbs[name].materials[name].SuperElasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        nonassociated
            None or a Float specifying the volumetric transformation strain. If
            **nonassociated**=None, the value of the volumetric transformation strain is equal to the
            uniaxial transformation strain. The default value is None.

        Returns
        -------
            A SuperElasticity object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the SuperElasticity object.

        Raises
        ------
        RangeError
        """
        pass
