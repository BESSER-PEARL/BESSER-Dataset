





import java.util.List;
import java.util.ArrayList;

public class journal_article  {

    private None AuthoredBy;
    private int Year;
    private None Publisher;
    private int Volume;
    private int Pages;
    private String Title;
    private String JournalName;



    public journal_article(
        None AuthoredBy,        int Year,        None Publisher,        int Volume,        int Pages,        String Title,        String JournalName    ) {
        this.AuthoredBy = AuthoredBy;
        this.Year = Year;
        this.Publisher = Publisher;
        this.Volume = Volume;
        this.Pages = Pages;
        this.Title = Title;
        this.JournalName = JournalName;
    }


    public None getAuthoredby() {
        return AuthoredBy;
    }

    public void setAuthoredby(None AuthoredBy) {
        this.AuthoredBy = AuthoredBy;
    }
    public int getYear() {
        return Year;
    }

    public void setYear(int Year) {
        this.Year = Year;
    }
    public None getPublisher() {
        return Publisher;
    }

    public void setPublisher(None Publisher) {
        this.Publisher = Publisher;
    }
    public int getVolume() {
        return Volume;
    }

    public void setVolume(int Volume) {
        this.Volume = Volume;
    }
    public int getPages() {
        return Pages;
    }

    public void setPages(int Pages) {
        this.Pages = Pages;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public String getJournalname() {
        return JournalName;
    }

    public void setJournalname(String JournalName) {
        this.JournalName = JournalName;
    }


}