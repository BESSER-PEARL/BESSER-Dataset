





import java.util.List;
import java.util.ArrayList;

public class patron  {

    private String search;
    private String request;
    private String details;
    private String patronid;
    private String payfine;





    private book_mdatabase book_mdatabase;


    public patron(
        String search,        String request,        String details,        String patronid,        String payfine    ) {
        this.search = search;
        this.request = request;
        this.details = details;
        this.patronid = patronid;
        this.payfine = payfine;
    }


    public String getSearch() {
        return search;
    }

    public void setSearch(String search) {
        this.search = search;
    }
    public String getRequest() {
        return request;
    }

    public void setRequest(String request) {
        this.request = request;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public String getPatronid() {
        return patronid;
    }

    public void setPatronid(String patronid) {
        this.patronid = patronid;
    }
    public String getPayfine() {
        return payfine;
    }

    public void setPayfine(String payfine) {
        this.payfine = payfine;
    }

    public book_mdatabase getBook_mdatabase() {
        return book_mdatabase;
    }

    public void setBook_mdatabase(book_mdatabase book_mdatabase) {
        this.book_mdatabase = book_mdatabase;
    }

}