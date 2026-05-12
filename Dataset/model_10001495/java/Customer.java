





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Address;
    private String Id;
    private String Name;





    private Bank bank;


    public Customer(
        String Address,        String Id,        String Name    ) {
        this.Address = Address;
        this.Id = Id;
        this.Name = Name;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}