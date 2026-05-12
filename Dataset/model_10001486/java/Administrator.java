





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private int Id;





    private Account account;


    public Administrator(
        int Id    ) {
        this.Id = Id;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}