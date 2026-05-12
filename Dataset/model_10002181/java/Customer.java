





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Password;
    private String Email;
    private String Address;
    private String Name;
    private int Phone;
    private String Accontbalance;
    private int ID;



    public Customer(
        String Password,        String Email,        String Address,        String Name,        int Phone,        String Accontbalance,        int ID    ) {
        this.Password = Password;
        this.Email = Email;
        this.Address = Address;
        this.Name = Name;
        this.Phone = Phone;
        this.Accontbalance = Accontbalance;
        this.ID = ID;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getAccontbalance() {
        return Accontbalance;
    }

    public void setAccontbalance(String Accontbalance) {
        this.Accontbalance = Accontbalance;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}