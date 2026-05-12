





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int number;
    private int balance;





    private Customer customer;




    private Bank bank;


    public Account(
        int number,        int balance    ) {
        this.number = number;
        this.balance = balance;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
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