





import java.util.List;
import java.util.ArrayList;

public class ATM  {

    private String location;
    private String managedby;





    private Bank bank;


    public ATM(
        String location,        String managedby    ) {
        this.location = location;
        this.managedby = managedby;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getManagedby() {
        return managedby;
    }

    public void setManagedby(String managedby) {
        this.managedby = managedby;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}