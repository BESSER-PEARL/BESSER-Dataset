





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private String address;
    private String phone;
    private String Cust_id;





    private Current_Account current_account;




    private Saving_Account saving_account;


    public Customer(
        String name,        String address,        String phone,        String Cust_id    ) {
        this.name = name;
        this.address = address;
        this.phone = phone;
        this.Cust_id = Cust_id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getCust_id() {
        return Cust_id;
    }

    public void setCust_id(String Cust_id) {
        this.Cust_id = Cust_id;
    }

    public Current_Account getCurrent_account() {
        return current_account;
    }

    public void setCurrent_account(Current_Account current_account) {
        this.current_account = current_account;
    }
    public Saving_Account getSaving_account() {
        return saving_account;
    }

    public void setSaving_account(Saving_Account saving_account) {
        this.saving_account = saving_account;
    }

}