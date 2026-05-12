





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String user_id;
    private String text;
    private String id;





    private Expense expense;


    public Comment(
        String user_id,        String text,        String id    ) {
        this.user_id = user_id;
        this.text = text;
        this.id = id;
    }


    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Expense getExpense() {
        return expense;
    }

    public void setExpense(Expense expense) {
        this.expense = expense;
    }

}