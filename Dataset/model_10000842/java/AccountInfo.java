





import java.util.List;
import java.util.ArrayList;

public class AccountInfo  {

    private String bankBranch;
    private int routingNumber;
    private String name;
    private int ID;
    private String bankName;
    private int accountNumber;





    private Farmer farmer;


    public AccountInfo(
        String bankBranch,        int routingNumber,        String name,        int ID,        String bankName,        int accountNumber    ) {
        this.bankBranch = bankBranch;
        this.routingNumber = routingNumber;
        this.name = name;
        this.ID = ID;
        this.bankName = bankName;
        this.accountNumber = accountNumber;
    }


    public String getBankbranch() {
        return bankBranch;
    }

    public void setBankbranch(String bankBranch) {
        this.bankBranch = bankBranch;
    }
    public int getRoutingnumber() {
        return routingNumber;
    }

    public void setRoutingnumber(int routingNumber) {
        this.routingNumber = routingNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getBankname() {
        return bankName;
    }

    public void setBankname(String bankName) {
        this.bankName = bankName;
    }
    public int getAccountnumber() {
        return accountNumber;
    }

    public void setAccountnumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public Farmer getFarmer() {
        return farmer;
    }

    public void setFarmer(Farmer farmer) {
        this.farmer = farmer;
    }

}