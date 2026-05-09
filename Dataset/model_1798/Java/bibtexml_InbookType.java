





import java.util.List;
import java.util.ArrayList;

public class bibtexml_InbookType  {

    private String edition;
    private String chapter;
    private String year;
    private String crossref;
    private String volume;
    private String key;
    private String editor;
    private String publisher;
    private String address;
    private String note;
    private String series;
    private String number;
    private String type;
    private String url;
    private String pages;
    private String month;
    private String doi;
    private String pages1;
    private String author;
    private String title;





    private bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass;


    public bibtexml_InbookType(
        String edition,        String chapter,        String year,        String crossref,        String volume,        String key,        String editor,        String publisher,        String address,        String note,        String series,        String number,        String type,        String url,        String pages,        String month,        String doi,        String pages1,        String author,        String title    ) {
        this.edition = edition;
        this.chapter = chapter;
        this.year = year;
        this.crossref = crossref;
        this.volume = volume;
        this.key = key;
        this.editor = editor;
        this.publisher = publisher;
        this.address = address;
        this.note = note;
        this.series = series;
        this.number = number;
        this.type = type;
        this.url = url;
        this.pages = pages;
        this.month = month;
        this.doi = doi;
        this.pages1 = pages1;
        this.author = author;
        this.title = title;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getCrossref() {
        return crossref;
    }

    public void setCrossref(String crossref) {
        this.crossref = crossref;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
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
    public String getPages1() {
        return pages1;
    }

    public void setPages1(String pages1) {
        this.pages1 = pages1;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bibtexml_BibTeXMLEntriesClass getBibtexml_bibtexmlentriesclass() {
        return bibtexml_bibtexmlentriesclass;
    }

    public void setBibtexml_bibtexmlentriesclass(bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass) {
        this.bibtexml_bibtexmlentriesclass = bibtexml_bibtexmlentriesclass;
    }

}