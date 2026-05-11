





import java.util.List;
import java.util.ArrayList;

public class carnot_TriggerType extends ITypedElement, IIdentifiableModelElement, IAccessPointOwner {






    private carnot_ProcessDefinitionType carnot_processdefinitiontype;




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


    public carnot_ProcessDefinitionType getCarnot_processdefinitiontype() {
        return carnot_processdefinitiontype;
    }

    public void setCarnot_processdefinitiontype(carnot_ProcessDefinitionType carnot_processdefinitiontype) {
        this.carnot_processdefinitiontype = carnot_processdefinitiontype;
    }
    public List<carnot_ParameterMappingType> getCarnot_parametermappingtypes() {
        return carnot_parametermappingtypes;
    }

    public void addCarnot_parametermappingtype(Carnot_parametermappingtype carnot_parametermappingtype) {
        this.carnot_parametermappingtypes.add(carnot_parametermappingtype);
    }

}