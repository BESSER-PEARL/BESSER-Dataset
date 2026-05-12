





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String categoryName;
    private int categoryID;





    private List<Book> books;




    private Category category;


    public Category(
        String categoryName,        int categoryID    ) {
        this.categoryName = categoryName;
        this.categoryID = categoryID;
        this.books = new ArrayList<>();
    }

    public Category(
        String categoryName,        int categoryID        ArrayList<Book> books    ) {
        this.categoryName = categoryName;
        this.categoryID = categoryID;
        this.books = books;
    }

    public String getCategoryname() {
        return categoryName;
    }

    public void setCategoryname(String categoryName) {
        this.categoryName = categoryName;
    }
    public int getCategoryid() {
        return categoryID;
    }

    public void setCategoryid(int categoryID) {
        this.categoryID = categoryID;
    }

    public List<Book> getBooks() {
        return books;
    }

    public void addBook(Book book) {
        this.books.add(book);
    }
    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }

}