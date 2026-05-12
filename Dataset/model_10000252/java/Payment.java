





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String comments;
    private int total;
    private int id;



    public Payment(
        String comments,        int total,        int id    ) {
        this.comments = comments;
        this.total = total;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}