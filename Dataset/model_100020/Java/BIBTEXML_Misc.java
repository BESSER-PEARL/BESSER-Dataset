





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Misc extends Entry {

    private String note;
    private String month;
    private String howpublished;
    private String year;
    private String title;



    public BIBTEXML_Misc(
        String note,        String month,        String howpublished,        String year,        String title    ) {
        super(
        );
        this.note = note;
        this.month = month;
        this.howpublished = howpublished;
        this.year = year;
        this.title = title;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}