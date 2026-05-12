





import java.util.List;
import java.util.ArrayList;

public class core_Actor extends IdentifiedElement {

    private String phoneNumber;
    private String address;
    private String email;





    private core_SystemContext core_systemcontext;




    private List<core_Interaction> core_interactions;




    private core_ContractualElement core_contractualelement;


    public core_Actor(
        String phoneNumber,        String address,        String email    ) {
        super(
        );
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.email = email;
        this.core_interactions = new ArrayList<>();
    }

    public core_Actor(
        String phoneNumber,        String address,        String email        ArrayList<core_Interaction> core_interactions    ) {
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.email = email;
        this.core_interactions = core_interactions;
    }

    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
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

    public core_SystemContext getCore_systemcontext() {
        return core_systemcontext;
    }

    public void setCore_systemcontext(core_SystemContext core_systemcontext) {
        this.core_systemcontext = core_systemcontext;
    }
    public List<core_Interaction> getCore_interactions() {
        return core_interactions;
    }

    public void addCore_interaction(Core_interaction core_interaction) {
        this.core_interactions.add(core_interaction);
    }
    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}