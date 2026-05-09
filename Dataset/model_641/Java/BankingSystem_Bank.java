





import java.util.List;
import java.util.ArrayList;

public class BankingSystem_Bank  {

    private String name;
    private String description;
    private int bankId;



    public BankingSystem_Bank(
        String name,        String description,        int bankId    ) {
        this.name = name;
        this.description = description;
        this.bankId = bankId;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getBankid() {
        return bankId;
    }

    public void setBankid(int bankId) {
        this.bankId = bankId;
    }


}