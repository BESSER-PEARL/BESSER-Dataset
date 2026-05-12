





import java.util.List;
import java.util.ArrayList;

public class bibtex_Document  {

    private String year;
    private String authors;
    private String doi;
    private int cites;
    private String type;
    private String month;
    private String url;
    private String key;
    private String title;
    private String file;
    private String abstract;
    private String unparsedAuthors;





    private bibtex_Model bibtex_model;


    public bibtex_Document(
        String year,        String authors,        String doi,        int cites,        String type,        String month,        String url,        String key,        String title,        String file,        String abstract,        String unparsedAuthors    ) {
        this.year = year;
        this.authors = authors;
        this.doi = doi;
        this.cites = cites;
        this.type = type;
        this.month = month;
        this.url = url;
        this.key = key;
        this.title = title;
        this.file = file;
        this.abstract = abstract;
        this.unparsedAuthors = unparsedAuthors;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }
    public int getCites() {
        return cites;
    }

    public void setCites(int cites) {
        this.cites = cites;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getUnparsedauthors() {
        return unparsedAuthors;
    }

    public void setUnparsedauthors(String unparsedAuthors) {
        this.unparsedAuthors = unparsedAuthors;
    }

    public bibtex_Model getBibtex_model() {
        return bibtex_model;
    }

    public void setBibtex_model(bibtex_Model bibtex_model) {
        this.bibtex_model = bibtex_model;
    }

}