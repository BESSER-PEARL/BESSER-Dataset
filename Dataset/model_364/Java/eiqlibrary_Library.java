





import java.util.List;
import java.util.ArrayList;

public class eiqlibrary_Library  {

    private int sumOfPages;
    private String address;
    private int requestCount;
    private int internalRequestCount;





    private List<eiqlibrary_Book> eiqlibrary_books;




    private List<eiqlibrary_Book> eiqlibrary_books;


    public eiqlibrary_Library(
        int sumOfPages,        String address,        int requestCount,        int internalRequestCount    ) {
        this.sumOfPages = sumOfPages;
        this.address = address;
        this.requestCount = requestCount;
        this.internalRequestCount = internalRequestCount;
        this.eiqlibrary_books = new ArrayList<>();
        this.eiqlibrary_books = new ArrayList<>();
    }

    public eiqlibrary_Library(
        int sumOfPages,        String address,        int requestCount,        int internalRequestCount        ArrayList<eiqlibrary_Book> eiqlibrary_books,        ArrayList<eiqlibrary_Book> eiqlibrary_books    ) {
        this.sumOfPages = sumOfPages;
        this.address = address;
        this.requestCount = requestCount;
        this.internalRequestCount = internalRequestCount;
        this.eiqlibrary_books = eiqlibrary_books;
        this.eiqlibrary_books = eiqlibrary_books;
    }

    public int getSumofpages() {
        return sumOfPages;
    }

    public void setSumofpages(int sumOfPages) {
        this.sumOfPages = sumOfPages;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getRequestcount() {
        return requestCount;
    }

    public void setRequestcount(int requestCount) {
        this.requestCount = requestCount;
    }
    public int getInternalrequestcount() {
        return internalRequestCount;
    }

    public void setInternalrequestcount(int internalRequestCount) {
        this.internalRequestCount = internalRequestCount;
    }

    public List<eiqlibrary_Book> getEiqlibrary_books() {
        return eiqlibrary_books;
    }

    public void addEiqlibrary_book(Eiqlibrary_book eiqlibrary_book) {
        this.eiqlibrary_books.add(eiqlibrary_book);
    }
    public List<eiqlibrary_Book> getEiqlibrary_books() {
        return eiqlibrary_books;
    }

    public void addEiqlibrary_book(Eiqlibrary_book eiqlibrary_book) {
        this.eiqlibrary_books.add(eiqlibrary_book);
    }

}