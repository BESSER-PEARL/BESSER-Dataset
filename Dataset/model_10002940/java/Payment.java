





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String comments;
    private int id;
    private int total;





    private Account account;


    public Payment(
        String comments,        int id,        int total    ) {
        this.comments = comments;
        this.id = id;
        this.total = total;
    }


    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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