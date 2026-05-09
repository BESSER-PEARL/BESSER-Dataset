





import java.util.List;
import java.util.ArrayList;

public class bibtexml_BookType  {

    private String key;
    private String note;
    private String title;
    private String author;
    private String address;
    private String series;
    private String volume;
    private String year;
    private String publisher;
    private String number;
    private String edition;
    private String doi;
    private String month;
    private String editor;
    private String crossref;
    private String url;





    private bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass;


    public bibtexml_BookType(
        String key,        String note,        String title,        String author,        String address,        String series,        String volume,        String year,        String publisher,        String number,        String edition,        String doi,        String month,        String editor,        String crossref,        String url    ) {
        this.key = key;
        this.note = note;
        this.title = title;
        this.author = author;
        this.address = address;
        this.series = series;
        this.volume = volume;
        this.year = year;
        this.publisher = publisher;
        this.number = number;
        this.edition = edition;
        this.doi = doi;
        this.month = month;
        this.editor = editor;
        this.crossref = crossref;
        this.url = url;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
    public String getCrossref() {
        return crossref;
    }

    public void setCrossref(String crossref) {
        this.crossref = crossref;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public bibtexml_BibTeXMLEntriesClass getBibtexml_bibtexmlentriesclass() {
        return bibtexml_bibtexmlentriesclass;
    }

    public void setBibtexml_bibtexmlentriesclass(bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass) {
        this.bibtexml_bibtexmlentriesclass = bibtexml_bibtexmlentriesclass;
    }

}