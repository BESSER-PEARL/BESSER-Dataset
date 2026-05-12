





import java.util.List;
import java.util.ArrayList;

public class Bibtex_BibtexEntry  {

    private String Author;
    private String Year;
    private String Journal;
    private String Pages;
    private String Volume;
    private String Title;
    private String Text;
    private String publicationFilePath;



    public Bibtex_BibtexEntry(
        String Author,        String Year,        String Journal,        String Pages,        String Volume,        String Title,        String Text,        String publicationFilePath    ) {
        this.Author = Author;
        this.Year = Year;
        this.Journal = Journal;
        this.Pages = Pages;
        this.Volume = Volume;
        this.Title = Title;
        this.Text = Text;
        this.publicationFilePath = publicationFilePath;
    }


    public String getAuthor() {
        return Author;
    }

    public void setAuthor(String Author) {
        this.Author = Author;
    }
    public String getYear() {
        return Year;
    }

    public void setYear(String Year) {
        this.Year = Year;
    }
    public String getJournal() {
        return Journal;
    }

    public void setJournal(String Journal) {
        this.Journal = Journal;
    }
    public String getPages() {
        return Pages;
    }

    public void setPages(String Pages) {
        this.Pages = Pages;
    }
    public String getVolume() {
        return Volume;
    }

    public void setVolume(String Volume) {
        this.Volume = Volume;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }
    public String getPublicationfilepath() {
        return publicationFilePath;
    }

    public void setPublicationfilepath(String publicationFilePath) {
        this.publicationFilePath = publicationFilePath;
    }


}