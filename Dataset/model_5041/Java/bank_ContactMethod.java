





import java.util.List;
import java.util.ArrayList;

public class bank_ContactMethod  {

    private String name;
    private String description;





    private bank_Party bank_party;


    public bank_ContactMethod(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
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

    public bank_Party getBank_party() {
        return bank_party;
    }

    public void setBank_party(bank_Party bank_party) {
        this.bank_party = bank_party;
    }

}