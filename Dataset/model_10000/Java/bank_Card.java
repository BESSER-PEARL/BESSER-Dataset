





import java.util.List;
import java.util.ArrayList;

public class bank_Card  {

    private String number;
    private String type;





    private bank_Account bank_account;


    public bank_Card(
        String number,        String type    ) {
        this.number = number;
        this.type = type;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public bank_Account getBank_account() {
        return bank_account;
    }

    public void setBank_account(bank_Account bank_account) {
        this.bank_account = bank_account;
    }

}