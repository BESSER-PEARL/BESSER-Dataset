





import java.util.List;
import java.util.ArrayList;

public class bibtex_Article extends DatedEntry, Entries, MonthEntry, AuthoredEntry {

    private int pages;
    private String note;
    private int volume;
    private String journal;
    private int number;



    public bibtex_Article(
        int pages,        String note,        int volume,        String journal,        int number    ) {
        super(
        );
        this.pages = pages;
        this.note = note;
        this.volume = volume;
        this.journal = journal;
        this.number = number;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }
    public String getJournal() {
        return journal;
    }

    public void setJournal(String journal) {
        this.journal = journal;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}