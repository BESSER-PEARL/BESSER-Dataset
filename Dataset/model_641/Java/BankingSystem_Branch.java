





import java.util.List;
import java.util.ArrayList;

public class BankingSystem_Branch  {

    private String location;
    private String name;
    private int branchId;
    private String phoneNumber;





    private BankingSystem_Bank bankingsystem_bank;




    private BankingSystem_Bank bankingsystem_bank;


    public BankingSystem_Branch(
        String location,        String name,        int branchId,        String phoneNumber    ) {
        this.location = location;
        this.name = name;
        this.branchId = branchId;
        this.phoneNumber = phoneNumber;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getBranchid() {
        return branchId;
    }

    public void setBranchid(int branchId) {
        this.branchId = branchId;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public BankingSystem_Bank getBankingsystem_bank() {
        return bankingsystem_bank;
    }

    public void setBankingsystem_bank(BankingSystem_Bank bankingsystem_bank) {
        this.bankingsystem_bank = bankingsystem_bank;
    }
    public BankingSystem_Bank getBankingsystem_bank() {
        return bankingsystem_bank;
    }

    public void setBankingsystem_bank(BankingSystem_Bank bankingsystem_bank) {
        this.bankingsystem_bank = bankingsystem_bank;
    }

}