





import java.util.List;
import java.util.ArrayList;

public class Implementation_StaffComponent_Employee  {

    private String name;
    private String email;
    private String ssn;
    private String password;
    private String id;
    private String phone;





    private Implementation_StaffComponent_AccountManager implementation_staffcomponent_accountmanager;




    private Implementation_StaffComponent_AccountManager implementation_staffcomponent_accountmanager;


    public Implementation_StaffComponent_Employee(
        String name,        String email,        String ssn,        String password,        String id,        String phone    ) {
        this.name = name;
        this.email = email;
        this.ssn = ssn;
        this.password = password;
        this.id = id;
        this.phone = phone;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public Implementation_StaffComponent_AccountManager getImplementation_staffcomponent_accountmanager() {
        return implementation_staffcomponent_accountmanager;
    }

    public void setImplementation_staffcomponent_accountmanager(Implementation_StaffComponent_AccountManager implementation_staffcomponent_accountmanager) {
        this.implementation_staffcomponent_accountmanager = implementation_staffcomponent_accountmanager;
    }
    public Implementation_StaffComponent_AccountManager getImplementation_staffcomponent_accountmanager() {
        return implementation_staffcomponent_accountmanager;
    }

    public void setImplementation_staffcomponent_accountmanager(Implementation_StaffComponent_AccountManager implementation_staffcomponent_accountmanager) {
        this.implementation_staffcomponent_accountmanager = implementation_staffcomponent_accountmanager;
    }

}