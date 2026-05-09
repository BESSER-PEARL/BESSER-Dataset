





import java.util.List;
import java.util.ArrayList;

public class bibtexml_InbookType  {

    private String doi;
    private String number;
    private String pages;
    private String edition;
    private String type;
    private String pages1;
    private String key;
    private String note;
    private String volume;
    private String series;
    private String author;
    private String url;
    private String crossref;
    private String address;
    private String publisher;
    private String year;
    private String chapter;
    private String editor;
    private String month;
    private String title;





    private bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass;


    public bibtexml_InbookType(
        String doi,        String number,        String pages,        String edition,        String type,        String pages1,        String key,        String note,        String volume,        String series,        String author,        String url,        String crossref,        String address,        String publisher,        String year,        String chapter,        String editor,        String month,        String title    ) {
        this.doi = doi;
        this.number = number;
        this.pages = pages;
        this.edition = edition;
        this.type = type;
        this.pages1 = pages1;
        this.key = key;
        this.note = note;
        this.volume = volume;
        this.series = series;
        this.author = author;
        this.url = url;
        this.crossref = crossref;
        this.address = address;
        this.publisher = publisher;
        this.year = year;
        this.chapter = chapter;
        this.editor = editor;
        this.month = month;
        this.title = title;
    }


    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPages1() {
        return pages1;
    }

    public void setPages1(String pages1) {
        this.pages1 = pages1;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
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
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
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
    public String getCrossref() {
        return crossref;
    }

    public void setCrossref(String crossref) {
        this.crossref = crossref;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }
    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
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