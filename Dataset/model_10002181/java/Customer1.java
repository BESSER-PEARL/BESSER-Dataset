





import java.util.List;
import java.util.ArrayList;

public class Customer1  {

    private String _attr;
    private String Adress;
    private int Phone;
    private String Password;
    private String attribute;
    private int ID;
    private String Address;
    private String Accontbalance;
    private String Name;
    private String Email;



    public Customer1(
        String _attr,        String Adress,        int Phone,        String Password,        String attribute,        int ID,        String Address,        String Accontbalance,        String Name,        String Email    ) {
        this._attr = _attr;
        this.Adress = Adress;
        this.Phone = Phone;
        this.Password = Password;
        this.attribute = attribute;
        this.ID = ID;
        this.Address = Address;
        this.Accontbalance = Accontbalance;
        this.Name = Name;
        this.Email = Email;
    }


    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public String getAdress() {
        return Adress;
    }

    public void setAdress(String Adress) {
        this.Adress = Adress;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getAccontbalance() {
        return Accontbalance;
    }

    public void setAccontbalance(String Accontbalance) {
        this.Accontbalance = Accontbalance;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}