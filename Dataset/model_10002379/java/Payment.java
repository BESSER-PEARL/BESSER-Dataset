





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int total;
    private int id;
    private String comments;





    private Account account;


    public Payment(
        int total,        int id,        String comments    ) {
        this.total = total;
        this.id = id;
        this.comments = comments;
    }


    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}