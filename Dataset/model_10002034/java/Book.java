





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private int categoryID;
    private int rating;
    private String productURL;
    private String authorName;
    private String price;
    private String notes;
    private String bookName;
    private String imageURL;
    private int bookID;





    private BooksOrder booksorder;


    public Book(
        int categoryID,        int rating,        String productURL,        String authorName,        String price,        String notes,        String bookName,        String imageURL,        int bookID    ) {
        this.categoryID = categoryID;
        this.rating = rating;
        this.productURL = productURL;
        this.authorName = authorName;
        this.price = price;
        this.notes = notes;
        this.bookName = bookName;
        this.imageURL = imageURL;
        this.bookID = bookID;
    }


    public int getCategoryid() {
        return categoryID;
    }

    public void setCategoryid(int categoryID) {
        this.categoryID = categoryID;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getProducturl() {
        return productURL;
    }

    public void setProducturl(String productURL) {
        this.productURL = productURL;
    }
    public String getAuthorname() {
        return authorName;
    }

    public void setAuthorname(String authorName) {
        this.authorName = authorName;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public String getBookname() {
        return bookName;
    }

    public void setBookname(String bookName) {
        this.bookName = bookName;
    }
    public String getImageurl() {
        return imageURL;
    }

    public void setImageurl(String imageURL) {
        this.imageURL = imageURL;
    }
    public int getBookid() {
        return bookID;
    }

    public void setBookid(int bookID) {
        this.bookID = bookID;
    }

    public BooksOrder getBooksorder() {
        return booksorder;
    }

    public void setBooksorder(BooksOrder booksorder) {
        this.booksorder = booksorder;
    }

}