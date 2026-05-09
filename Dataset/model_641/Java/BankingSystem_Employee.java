





import java.util.List;
import java.util.ArrayList;

public class BankingSystem_Employee  {

    private String eaddress;
    private int eage;
    private boolean isCustomer;
    private String ephoneNumber;
    private String ename;
    private int eid;





    private BankingSystem_Branch bankingsystem_branch;




    private BankingSystem_Branch bankingsystem_branch;


    public BankingSystem_Employee(
        String eaddress,        int eage,        boolean isCustomer,        String ephoneNumber,        String ename,        int eid    ) {
        this.eaddress = eaddress;
        this.eage = eage;
        this.isCustomer = isCustomer;
        this.ephoneNumber = ephoneNumber;
        this.ename = ename;
        this.eid = eid;
    }


    public String getEaddress() {
        return eaddress;
    }

    public void setEaddress(String eaddress) {
        this.eaddress = eaddress;
    }
    public int getEage() {
        return eage;
    }

    public void setEage(int eage) {
        this.eage = eage;
    }
    public boolean getIscustomer() {
        return isCustomer;
    }

    public void setIscustomer(boolean isCustomer) {
        this.isCustomer = isCustomer;
    }
    public String getEphonenumber() {
        return ephoneNumber;
    }

    public void setEphonenumber(String ephoneNumber) {
        this.ephoneNumber = ephoneNumber;
    }
    public String getEname() {
        return ename;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }
    public int getEid() {
        return eid;
    }

    public void setEid(int eid) {
        this.eid = eid;
    }

    public BankingSystem_Branch getBankingsystem_branch() {
        return bankingsystem_branch;
    }

    public void setBankingsystem_branch(BankingSystem_Branch bankingsystem_branch) {
        this.bankingsystem_branch = bankingsystem_branch;
    }
    public BankingSystem_Branch getBankingsystem_branch() {
        return bankingsystem_branch;
    }

    public void setBankingsystem_branch(BankingSystem_Branch bankingsystem_branch) {
        this.bankingsystem_branch = bankingsystem_branch;
    }

}