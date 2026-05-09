





import java.util.List;
import java.util.ArrayList;

public class bibtexml_InproceedingsType  {

    private String year;
    private String number;
    private String title;
    private String key;
    private String booktitle;
    private String volume;
    private String organization;
    private String editor;
    private String series;
    private String publisher;
    private String doi;
    private String address;
    private String note;
    private String month;
    private String pages;
    private String url;
    private String crossref;
    private String author;





    private bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass;


    public bibtexml_InproceedingsType(
        String year,        String number,        String title,        String key,        String booktitle,        String volume,        String organization,        String editor,        String series,        String publisher,        String doi,        String address,        String note,        String month,        String pages,        String url,        String crossref,        String author    ) {
        this.year = year;
        this.number = number;
        this.title = title;
        this.key = key;
        this.booktitle = booktitle;
        this.volume = volume;
        this.organization = organization;
        this.editor = editor;
        this.series = series;
        this.publisher = publisher;
        this.doi = doi;
        this.address = address;
        this.note = note;
        this.month = month;
        this.pages = pages;
        this.url = url;
        this.crossref = crossref;
        this.author = author;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getBooktitle() {
        return booktitle;
    }

    public void setBooktitle(String booktitle) {
        this.booktitle = booktitle;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
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
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public bibtexml_BibTeXMLEntriesClass getBibtexml_bibtexmlentriesclass() {
        return bibtexml_bibtexmlentriesclass;
    }

    public void setBibtexml_bibtexmlentriesclass(bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass) {
        this.bibtexml_bibtexmlentriesclass = bibtexml_bibtexmlentriesclass;
    }

}