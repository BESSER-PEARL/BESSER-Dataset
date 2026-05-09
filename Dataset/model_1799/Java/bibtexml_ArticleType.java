





import java.util.List;
import java.util.ArrayList;

public class bibtexml_ArticleType  {

    private String note;
    private String title;
    private String volume;
    private String month;
    private String doi;
    private String year;
    private String author;
    private String url;
    private String number;
    private String crossref;
    private String journal;
    private String key;
    private String pages;



    public bibtexml_ArticleType(
        String note,        String title,        String volume,        String month,        String doi,        String year,        String author,        String url,        String number,        String crossref,        String journal,        String key,        String pages    ) {
        this.note = note;
        this.title = title;
        this.volume = volume;
        this.month = month;
        this.doi = doi;
        this.year = year;
        this.author = author;
        this.url = url;
        this.number = number;
        this.crossref = crossref;
        this.journal = journal;
        this.key = key;
        this.pages = pages;
    }


    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
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
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }


}