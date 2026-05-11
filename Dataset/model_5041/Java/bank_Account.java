





import java.util.List;
import java.util.ArrayList;

public class bank_Account  {

    private String balance;
    private int periodStart;
    private String number;
    private String description;



    public bank_Account(
        String balance,        int periodStart,        String number,        String description    ) {
        this.balance = balance;
        this.periodStart = periodStart;
        this.number = number;
        this.description = description;
    }


    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }
    public int getPeriodstart() {
        return periodStart;
    }

    public void setPeriodstart(int periodStart) {
        this.periodStart = periodStart;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}