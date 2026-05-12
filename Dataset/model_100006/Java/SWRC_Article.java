





import java.util.List;
import java.util.ArrayList;

public class SWRC_Article extends Publication {

    private String pages;
    private String journal;
    private String volume;
    private String number;
    private String month;



    public SWRC_Article(
        String pages,        String journal,        String volume,        String number,        String month    ) {
        super(
        );
        this.pages = pages;
        this.journal = journal;
        this.volume = volume;
        this.number = number;
        this.month = month;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getJournal() {
        return journal;
    }

    public void setJournal(String journal) {
        this.journal = journal;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}