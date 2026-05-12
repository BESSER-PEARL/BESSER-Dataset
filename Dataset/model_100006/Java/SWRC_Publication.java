





import java.util.List;
import java.util.ArrayList;

public class SWRC_Publication  {

    private String keywords;
    private String year;
    private String title;
    private String abstract;
    private String note;



    public SWRC_Publication(
        String keywords,        String year,        String title,        String abstract,        String note    ) {
        this.keywords = keywords;
        this.year = year;
        this.title = title;
        this.abstract = abstract;
        this.note = note;
    }


    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
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
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }


}