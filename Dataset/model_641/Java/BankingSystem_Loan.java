





import java.util.List;
import java.util.ArrayList;

public class BankingSystem_Loan  {

    private int duration;
    private float interestRate;
    private String loanNumber;
    private float amount;





    private BankingSystem_Customer bankingsystem_customer;




    private BankingSystem_Customer bankingsystem_customer;


    public BankingSystem_Loan(
        int duration,        float interestRate,        String loanNumber,        float amount    ) {
        this.duration = duration;
        this.interestRate = interestRate;
        this.loanNumber = loanNumber;
        this.amount = amount;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }
    public String getLoannumber() {
        return loanNumber;
    }

    public void setLoannumber(String loanNumber) {
        this.loanNumber = loanNumber;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }

    public BankingSystem_Customer getBankingsystem_customer() {
        return bankingsystem_customer;
    }

    public void setBankingsystem_customer(BankingSystem_Customer bankingsystem_customer) {
        this.bankingsystem_customer = bankingsystem_customer;
    }
    public BankingSystem_Customer getBankingsystem_customer() {
        return bankingsystem_customer;
    }

    public void setBankingsystem_customer(BankingSystem_Customer bankingsystem_customer) {
        this.bankingsystem_customer = bankingsystem_customer;
    }

}