





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Article extends DatedEntry, JournalEntry, TitledEntry, AuthoredEntry {

    private String number;
    private String note;
    private String pages;
    private String volume;



    public BIBTEXML_Article(
        String number,        String note,        String pages,        String volume    ) {
        super(
        );
        this.number = number;
        this.note = note;
        this.pages = pages;
        this.volume = volume;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }


}