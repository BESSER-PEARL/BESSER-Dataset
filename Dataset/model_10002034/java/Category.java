





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private int categoryID;
    private String categoryName;





    private Book book;




    private SessionManager sessionmanager;


    public Category(
        int categoryID,        String categoryName    ) {
        this.categoryID = categoryID;
        this.categoryName = categoryName;
    }


    public int getCategoryid() {
        return categoryID;
    }

    public void setCategoryid(int categoryID) {
        this.categoryID = categoryID;
    }
    public String getCategoryname() {
        return categoryName;
    }

    public void setCategoryname(String categoryName) {
        this.categoryName = categoryName;
    }

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }
    public SessionManager getSessionmanager() {
        return sessionmanager;
    }

    public void setSessionmanager(SessionManager sessionmanager) {
        this.sessionmanager = sessionmanager;
    }

}