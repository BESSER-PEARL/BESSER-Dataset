





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Misc extends Entry {

    private String title;
    private String month;
    private String year;
    private String note;
    private String howpublished;





    private List<Author> authors;


    public BIBTEXML_Misc(
        String title,        String month,        String year,        String note,        String howpublished    ) {
        super(
        );
        this.title = title;
        this.month = month;
        this.year = year;
        this.note = note;
        this.howpublished = howpublished;
        this.authors = new ArrayList<>();
    }

    public BIBTEXML_Misc(
        String title,        String month,        String year,        String note,        String howpublished        ArrayList<Author> authors    ) {
        this.title = title;
        this.month = month;
        this.year = year;
        this.note = note;
        this.howpublished = howpublished;
        this.authors = authors;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }

    public List<Author> getAuthors() {
        return authors;
    }

    public void addAuthor(Author author) {
        this.authors.add(author);
    }

}