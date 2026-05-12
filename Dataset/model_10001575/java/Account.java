





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String AccountNumber;
    private String Balance;





    private ATM__Transactions atm__transactions;




    private BANK bank;




    private Customer customer;


    public Account(
        String AccountNumber,        String Balance    ) {
        this.AccountNumber = AccountNumber;
        this.Balance = Balance;
    }


    public String getAccountnumber() {
        return AccountNumber;
    }

    public void setAccountnumber(String AccountNumber) {
        this.AccountNumber = AccountNumber;
    }
    public String getBalance() {
        return Balance;
    }

    public void setBalance(String Balance) {
        this.Balance = Balance;
    }

    public ATM__Transactions getAtm__transactions() {
        return atm__transactions;
    }

    public void setAtm__transactions(ATM__Transactions atm__transactions) {
        this.atm__transactions = atm__transactions;
    }
    public BANK getBank() {
        return bank;
    }

    public void setBank(BANK bank) {
        this.bank = bank;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}