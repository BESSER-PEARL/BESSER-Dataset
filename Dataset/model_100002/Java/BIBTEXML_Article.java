





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Article extends TitledEntry, AuthoredEntry, DatedEntry, JournalEntry {

    private String number;
    private String note;
    private String volume;
    private String pages;



    public BIBTEXML_Article(
        String number,        String note,        String volume,        String pages    ) {
        super(
        );
        this.number = number;
        this.note = note;
        this.volume = volume;
        this.pages = pages;
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
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }


}