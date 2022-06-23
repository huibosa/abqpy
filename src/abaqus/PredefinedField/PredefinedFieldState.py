from abaqusConstants import *


class PredefinedFieldState:
    """The PredefinedFieldState object is the base object for the objects in the
    predefinedFieldState repository of the Step object. The members of the
    PredefinedFieldState object are common to all objects derived from PredefinedFieldState.
    The PredefinedFieldState object has no constructor or methods.

    Attributes
    ----------
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the :py:class:`~abaqus.PredefinedField.:py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState`.:py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState`` object. Possible values are:
        
        - NOT_YET_ACTIVE
        - CREATED
        - PROPAGATED
        - MODIFIED
        - DEACTIVATED
        - DEACTIVATED_TO_INITIAL
        - NO_LONGER_ACTIVE
        - RESET_TO_INITIAL
        - TO_BE_COMPUTED
        - PROPAGATED_FROM_COMPUTED
        - BUILT_INTO_BASE_STATE
        - TYPE_NOT_APPLICABLE
        - INSTANCE_NOT_APPLICABLE
            
        This member exists in all :py:class:`~abaqus.PredefinedField.:py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState`.:py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState`` objects, but different predefined fields
        use different subsets of the entire list of possible values depending on propagation
        rules.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].steps[name].predefinedFieldStates[name]
    """

    #: A SymbolicConstant specifying the propagation state of the PredefinedFieldState object.
    #: Possible values are:
    #: 
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - DEACTIVATED_TO_INITIAL
    #: - NO_LONGER_ACTIVE
    #: - RESET_TO_INITIAL
    #: - TO_BE_COMPUTED
    #: - PROPAGATED_FROM_COMPUTED
    #: - BUILT_INTO_BASE_STATE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: This member exists in all PredefinedFieldState objects, but different predefined fields
    #: use different subsets of the entire list of possible values depending on propagation
    #: rules.
    status: SymbolicConstant = None
