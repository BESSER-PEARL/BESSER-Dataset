





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_TransactionReport  {

    private String name;
    private int totalEarned;
    private int balance;
    private int totalBurned;
    private int number;



    public RoyalAndLoyal_TransactionReport(
        String name,        int totalEarned,        int balance,        int totalBurned,        int number    ) {
        this.name = name;
        this.totalEarned = totalEarned;
        this.balance = balance;
        this.totalBurned = totalBurned;
        this.number = number;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTotalearned() {
        return totalEarned;
    }

    public void setTotalearned(int totalEarned) {
        this.totalEarned = totalEarned;
    }
    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }
    public int getTotalburned() {
        return totalBurned;
    }

    public void setTotalburned(int totalBurned) {
        this.totalBurned = totalBurned;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}