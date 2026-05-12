





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private int categoryID;
    private String categoryName;





    private Category category;




    private List<Book> books;


    public Category(
        int categoryID,        String categoryName    ) {
        this.categoryID = categoryID;
        this.categoryName = categoryName;
        this.books = new ArrayList<>();
    }

    public Category(
        int categoryID,        String categoryName        ArrayList<Book> books    ) {
        this.categoryID = categoryID;
        this.categoryName = categoryName;
        this.books = books;
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

    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }
    public List<Book> getBooks() {
        return books;
    }

    public void addBook(Book book) {
        this.books.add(book);
    }

}