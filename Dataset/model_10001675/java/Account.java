





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String number;
    private String balance;





    private Customer customer;




    private Bank bank;


    public Account(
        String number,        String balance    ) {
        this.number = number;
        this.balance = balance;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}