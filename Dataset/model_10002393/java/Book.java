





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private String dueDate;
    private String author;
    private String title;
    private int refNum;



    public Book(
        String dueDate,        String author,        String title,        int refNum    ) {
        this.dueDate = dueDate;
        this.author = author;
        this.title = title;
        this.refNum = refNum;
    }


    public String getDuedate() {
        return dueDate;
    }

    public void setDuedate(String dueDate) {
        this.dueDate = dueDate;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getRefnum() {
        return refNum;
    }

    public void setRefnum(int refNum) {
        this.refNum = refNum;
    }


}