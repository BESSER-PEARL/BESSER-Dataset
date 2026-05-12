





import java.util.List;
import java.util.ArrayList;

public class ATM_s  {

    private int PIN;
    private String OperatorName;
    private int Withdrawn;





    private Bank bank;


    public ATM_s(
        int PIN,        String OperatorName,        int Withdrawn    ) {
        this.PIN = PIN;
        this.OperatorName = OperatorName;
        this.Withdrawn = Withdrawn;
    }


    public int getPin() {
        return PIN;
    }

    public void setPin(int PIN) {
        this.PIN = PIN;
    }
    public String getOperatorname() {
        return OperatorName;
    }

    public void setOperatorname(String OperatorName) {
        this.OperatorName = OperatorName;
    }
    public int getWithdrawn() {
        return Withdrawn;
    }

    public void setWithdrawn(int Withdrawn) {
        this.Withdrawn = Withdrawn;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}