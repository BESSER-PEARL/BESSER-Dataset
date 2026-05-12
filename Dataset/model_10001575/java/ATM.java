





import java.util.List;
import java.util.ArrayList;

public class ATM  {

    private String location;
    private String ManagedBy;





    private BANK bank;


    public ATM(
        String location,        String ManagedBy    ) {
        this.location = location;
        this.ManagedBy = ManagedBy;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getManagedby() {
        return ManagedBy;
    }

    public void setManagedby(String ManagedBy) {
        this.ManagedBy = ManagedBy;
    }

    public BANK getBank() {
        return bank;
    }

    public void setBank(BANK bank) {
        this.bank = bank;
    }

}