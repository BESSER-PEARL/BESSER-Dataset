





import java.util.List;
import java.util.ArrayList;

public class AdvSearch  {

    private String bookHighCost;
    private String categoryID;
    private String bookTitle;
    private String bookAuthor;
    private String bookLowCost;





    private List<BookSet> booksets;


    public AdvSearch(
        String bookHighCost,        String categoryID,        String bookTitle,        String bookAuthor,        String bookLowCost    ) {
        this.bookHighCost = bookHighCost;
        this.categoryID = categoryID;
        this.bookTitle = bookTitle;
        this.bookAuthor = bookAuthor;
        this.bookLowCost = bookLowCost;
        this.booksets = new ArrayList<>();
    }

    public AdvSearch(
        String bookHighCost,        String categoryID,        String bookTitle,        String bookAuthor,        String bookLowCost        ArrayList<BookSet> booksets    ) {
        this.bookHighCost = bookHighCost;
        this.categoryID = categoryID;
        this.bookTitle = bookTitle;
        this.bookAuthor = bookAuthor;
        this.bookLowCost = bookLowCost;
        this.booksets = booksets;
    }

    public String getBookhighcost() {
        return bookHighCost;
    }

    public void setBookhighcost(String bookHighCost) {
        this.bookHighCost = bookHighCost;
    }
    public String getCategoryid() {
        return categoryID;
    }

    public void setCategoryid(String categoryID) {
        this.categoryID = categoryID;
    }
    public String getBooktitle() {
        return bookTitle;
    }

    public void setBooktitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }
    public String getBookauthor() {
        return bookAuthor;
    }

    public void setBookauthor(String bookAuthor) {
        this.bookAuthor = bookAuthor;
    }
    public String getBooklowcost() {
        return bookLowCost;
    }

    public void setBooklowcost(String bookLowCost) {
        this.bookLowCost = bookLowCost;
    }

    public List<BookSet> getBooksets() {
        return booksets;
    }

    public void addBookset(Bookset bookset) {
        this.booksets.add(bookset);
    }

}