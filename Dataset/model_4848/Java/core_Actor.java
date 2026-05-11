





import java.util.List;
import java.util.ArrayList;

public class core_Actor extends IdentifiedElement {

    private String address;
    private String email;
    private String phoneNumber;





    private core_ContractualElement core_contractualelement;


    public core_Actor(
        String address,        String email,        String phoneNumber    ) {
        super(
        );
        this.address = address;
        this.email = email;
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
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}