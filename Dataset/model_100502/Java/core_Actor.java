





import java.util.List;
import java.util.ArrayList;

public class core_Actor extends IdentifiedElement {

    private String address;
    private String email;
    private String phoneNumber;





    private List<core_EObject> core_eobjects;




    private core_ContractualElement core_contractualelement;




    private List<core_Interaction> core_interactions;




    private core_SystemContext core_systemcontext;


    public core_Actor(
        String address,        String email,        String phoneNumber    ) {
        super(
        );
        this.address = address;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.core_eobjects = new ArrayList<>();
        this.core_interactions = new ArrayList<>();
    }

    public core_Actor(
        String address,        String email,        String phoneNumber        ArrayList<core_EObject> core_eobjects,        ArrayList<core_Interaction> core_interactions    ) {
        this.address = address;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.core_eobjects = core_eobjects;
        this.core_interactions = core_interactions;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }
    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }
    public List<core_Interaction> getCore_interactions() {
        return core_interactions;
    }

    public void addCore_interaction(Core_interaction core_interaction) {
        this.core_interactions.add(core_interaction);
    }
    public core_SystemContext getCore_systemcontext() {
        return core_systemcontext;
    }

    public void setCore_systemcontext(core_SystemContext core_systemcontext) {
        this.core_systemcontext = core_systemcontext;
    }

}