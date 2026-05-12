





import java.util.List;
import java.util.ArrayList;

public class ATM  {

    private String managedby;
    private String location;





    private Bank bank;


    public ATM(
        String managedby,        String location    ) {
        this.managedby = managedby;
        this.location = location;
    }


    public String getManagedby() {
        return managedby;
    }

    public void setManagedby(String managedby) {
        this.managedby = managedby;
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