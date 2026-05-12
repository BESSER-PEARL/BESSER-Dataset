





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int Balance;
    private int AccountNumber;





    private Customer customer;




    private BANK bank;


    public Account(
        int Balance,        int AccountNumber    ) {
        this.Balance = Balance;
        this.AccountNumber = AccountNumber;
    }


    public int getBalance() {
        return Balance;
    }

    public void setBalance(int Balance) {
        this.Balance = Balance;
    }
    public int getAccountnumber() {
        return AccountNumber;
    }

    public void setAccountnumber(int AccountNumber) {
        this.AccountNumber = AccountNumber;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public BANK getBank() {
        return bank;
    }

    public void setBank(BANK bank) {
        this.bank = bank;
    }

}