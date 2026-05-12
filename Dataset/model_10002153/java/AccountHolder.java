





import java.util.List;
import java.util.ArrayList;

public class AccountHolder  {

    private int AccNo;
    private String Name;
    private String Address;





    private Accounts accounts;


    public AccountHolder(
        int AccNo,        String Name,        String Address    ) {
        this.AccNo = AccNo;
        this.Name = Name;
        this.Address = Address;
    }


    public int getAccno() {
        return AccNo;
    }

    public void setAccno(int AccNo) {
        this.AccNo = AccNo;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Accounts getAccounts() {
        return accounts;
    }

    public void setAccounts(Accounts accounts) {
        this.accounts = accounts;
    }

}