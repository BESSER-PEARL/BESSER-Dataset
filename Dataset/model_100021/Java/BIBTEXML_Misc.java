





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Misc extends Entry {

    private String title;
    private String note;
    private String howpublished;
    private String year;
    private String month;



    public BIBTEXML_Misc(
        String title,        String note,        String howpublished,        String year,        String month    ) {
        super(
        );
        this.title = title;
        this.note = note;
        this.howpublished = howpublished;
        this.year = year;
        this.month = month;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}