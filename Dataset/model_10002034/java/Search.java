





import java.util.List;
import java.util.ArrayList;

public class Search  {

    private String categoryID;
    private String bookTitle;





    private List<BookSet> booksets;


    public Search(
        String categoryID,        String bookTitle    ) {
        this.categoryID = categoryID;
        this.bookTitle = bookTitle;
        this.booksets = new ArrayList<>();
    }

    public Search(
        String categoryID,        String bookTitle        ArrayList<BookSet> booksets    ) {
        this.categoryID = categoryID;
        this.bookTitle = bookTitle;
        this.booksets = booksets;
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

    public List<BookSet> getBooksets() {
        return booksets;
    }

    public void addBookset(Bookset bookset) {
        this.booksets.add(bookset);
    }

}