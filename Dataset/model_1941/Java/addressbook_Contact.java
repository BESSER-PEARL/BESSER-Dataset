





import java.util.List;
import java.util.ArrayList;

public class addressbook_Contact extends Entry {

    private String lastName;
    private String firstName;
    private String email;





    private List<addressbook_Organization> addressbook_organizations;




    private addressbook_Organization addressbook_organization;


    public addressbook_Contact(
        String lastName,        String firstName,        String email    ) {
        super(
        );
        this.lastName = lastName;
        this.firstName = firstName;
        this.email = email;
        this.addressbook_organizations = new ArrayList<>();
    }

    public addressbook_Contact(
        String lastName,        String firstName,        String email        ArrayList<addressbook_Organization> addressbook_organizations    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.email = email;
        this.addressbook_organizations = addressbook_organizations;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<addressbook_Organization> getAddressbook_organizations() {
        return addressbook_organizations;
    }

    public void addAddressbook_organization(Addressbook_organization addressbook_organization) {
        this.addressbook_organizations.add(addressbook_organization);
    }
    public addressbook_Organization getAddressbook_organization() {
        return addressbook_organization;
    }

    public void setAddressbook_organization(addressbook_Organization addressbook_organization) {
        this.addressbook_organization = addressbook_organization;
    }

}