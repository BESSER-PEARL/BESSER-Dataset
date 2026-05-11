





import java.util.List;
import java.util.ArrayList;

public class carnot_TriggerType extends IIdentifiableModelElement, ITypedElement, IAccessPointOwner {






    private List<carnot_ParameterMappingType> carnot_parametermappingtypes;


    public carnot_TriggerType(
    ) {
        super(
        );
        this.carnot_parametermappingtypes = new ArrayList<>();
    }

    public carnot_TriggerType(
        ArrayList<carnot_ParameterMappingType> carnot_parametermappingtypes    ) {
        this.carnot_parametermappingtypes = carnot_parametermappingtypes;
    }


    public List<carnot_ParameterMappingType> getCarnot_parametermappingtypes() {
        return carnot_parametermappingtypes;
    }

    public void addCarnot_parametermappingtype(Carnot_parametermappingtype carnot_parametermappingtype) {
        this.carnot_parametermappingtypes.add(carnot_parametermappingtype);
    }

}