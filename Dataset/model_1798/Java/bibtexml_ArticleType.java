





import java.util.List;
import java.util.ArrayList;

public class bibtexml_ArticleType  {

    private String crossref;
    private String journal;
    private String volume;
    private String doi;
    private String note;
    private String pages;
    private String author;
    private String year;
    private String title;
    private String month;
    private String key;
    private String number;
    private String url;



    public bibtexml_ArticleType(
        String crossref,        String journal,        String volume,        String doi,        String note,        String pages,        String author,        String year,        String title,        String month,        String key,        String number,        String url    ) {
        this.crossref = crossref;
        this.journal = journal;
        this.volume = volume;
        this.doi = doi;
        this.note = note;
        this.pages = pages;
        this.author = author;
        this.year = year;
        this.title = title;
        this.month = month;
        this.key = key;
        this.number = number;
        this.url = url;
    }


    public String getCrossref() {
        return crossref;
    }

    public void setCrossref(String crossref) {
        this.crossref = crossref;
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
    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
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
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}