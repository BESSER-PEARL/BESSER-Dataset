





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int id;
    private String comments;
    private int total;





    private Account account;


    public Payment(
        int id,        String comments,        int total    ) {
        this.id = id;
        this.comments = comments;
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
    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}