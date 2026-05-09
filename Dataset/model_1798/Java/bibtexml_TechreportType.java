





import java.util.List;
import java.util.ArrayList;

public class bibtexml_TechreportType  {

    private String crossref;
    private String address;
    private String url;
    private String title;
    private String note;
    private String key;
    private String doi;
    private String type;
    private String number;
    private String year;
    private String institution;
    private String author;
    private String month;





    private bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass;


    public bibtexml_TechreportType(
        String crossref,        String address,        String url,        String title,        String note,        String key,        String doi,        String type,        String number,        String year,        String institution,        String author,        String month    ) {
        this.crossref = crossref;
        this.address = address;
        this.url = url;
        this.title = title;
        this.note = note;
        this.key = key;
        this.doi = doi;
        this.type = type;
        this.number = number;
        this.year = year;
        this.institution = institution;
        this.author = author;
        this.month = month;
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
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
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
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getInstitution() {
        return institution;
    }

    public void setInstitution(String institution) {
        this.institution = institution;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }

    public bibtexml_BibTeXMLEntriesClass getBibtexml_bibtexmlentriesclass() {
        return bibtexml_bibtexmlentriesclass;
    }

    public void setBibtexml_bibtexmlentriesclass(bibtexml_BibTeXMLEntriesClass bibtexml_bibtexmlentriesclass) {
        this.bibtexml_bibtexmlentriesclass = bibtexml_bibtexmlentriesclass;
    }

}