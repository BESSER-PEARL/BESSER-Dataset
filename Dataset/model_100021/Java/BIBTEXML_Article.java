





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Article extends AuthoredEntry, TitledEntry, DatedEntry, JournalEntry {

    private String note;
    private String pages;
    private String number;
    private String volume;



    public BIBTEXML_Article(
        String note,        String pages,        String number,        String volume    ) {
        super(
        );
        this.note = note;
        this.pages = pages;
        this.number = number;
        this.volume = volume;
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
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }


}