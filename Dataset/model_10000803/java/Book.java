





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private String title;
    private String author;
    private String dueDate;
    private int refNum;



    public Book(
        String title,        String author,        String dueDate,        int refNum    ) {
        this.title = title;
        this.author = author;
        this.dueDate = dueDate;
        this.refNum = refNum;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getDuedate() {
        return dueDate;
    }

    public void setDuedate(String dueDate) {
        this.dueDate = dueDate;
    }
    public int getRefnum() {
        return refNum;
    }

    public void setRefnum(int refNum) {
        this.refNum = refNum;
    }


}