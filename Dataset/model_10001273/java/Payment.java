





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int id;
    private int total;
    private String comments;





    private Account account;


    public Payment(
        int id,        int total,        String comments    ) {
        this.id = id;
        this.total = total;
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