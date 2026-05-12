





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private String location;
    private String BankId;



    public Bank(
        String location,        String BankId    ) {
        this.location = location;
        this.BankId = BankId;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getBankid() {
        return BankId;
    }

    public void setBankid(String BankId) {
        this.BankId = BankId;
    }


}