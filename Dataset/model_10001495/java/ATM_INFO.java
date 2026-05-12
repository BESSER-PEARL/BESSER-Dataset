





import java.util.List;
import java.util.ArrayList;

public class ATM_INFO  {

    private String Location;





    private Bank bank;


    public ATM_INFO(
        String Location    ) {
        this.Location = Location;
    }


    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}