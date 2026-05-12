





import java.util.List;
import java.util.ArrayList;

public class players_Person  {

    private String name;
    private String accountNumber;



    public players_Person(
        String name,        String accountNumber    ) {
        this.name = name;
        this.accountNumber = accountNumber;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccountnumber() {
        return accountNumber;
    }

    public void setAccountnumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }


}