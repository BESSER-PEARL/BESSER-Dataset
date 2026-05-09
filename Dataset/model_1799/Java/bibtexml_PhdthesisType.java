





import java.util.List;
import java.util.ArrayList;

public class bibtexml_PhdthesisType  {

    private String author;
    private String title;
    private String note;
    private String url;
    private String month;
    private String key;
    private String address;
    private String crossref;
    private String doi;
    private String year;
    private String type;
    private String school;





    private bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass;


    public bibtexml_PhdthesisType(
        String author,        String title,        String note,        String url,        String month,        String key,        String address,        String crossref,        String doi,        String year,        String type,        String school    ) {
        this.author = author;
        this.title = title;
        this.note = note;
        this.url = url;
        this.month = month;
        this.key = key;
        this.address = address;
        this.crossref = crossref;
        this.doi = doi;
        this.year = year;
        this.type = type;
        this.school = school;
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
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getCrossref() {
        return crossref;
    }

    public void setCrossref(String crossref) {
        this.crossref = crossref;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }

    public bibtexml_BibTeXMLEntriesClass getBibtexml_bibtexmlentriesclass() {
        return bibtexml_bibtexmlentriesclass;
    }

    public void setBibtexml_bibtexmlentriesclass(bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass) {
        this.bibtexml_bibtexmlentriesclass = bibtexml_bibtexmlentriesclass;
    }

}