





import java.util.List;
import java.util.ArrayList;

public class ATM  {

    private String managedBy;
    private String location;





    private Bank bank;


    public ATM(
        String managedBy,        String location    ) {
        this.managedBy = managedBy;
        this.location = location;
    }


    public String getManagedby() {
        return managedBy;
    }

    public void setManagedby(String managedBy) {
        this.managedBy = managedBy;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}