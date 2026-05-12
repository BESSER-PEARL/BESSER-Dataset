





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private String dueDate;
    private String title;
    private String author;
    private int refNum;



    public Book(
        String dueDate,        String title,        String author,        int refNum    ) {
        this.dueDate = dueDate;
        this.title = title;
        this.author = author;
        this.refNum = refNum;
    }


    public String getDuedate() {
        return dueDate;
    }

    public void setDuedate(String dueDate) {
        this.dueDate = dueDate;
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
    public int getRefnum() {
        return refNum;
    }

    public void setRefnum(int refNum) {
        this.refNum = refNum;
    }


}