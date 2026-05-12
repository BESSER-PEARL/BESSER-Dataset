





import java.util.List;
import java.util.ArrayList;

public class BookBorrow  {

    private None UserCode;
    private String InDate;
    private int BorrowID;
    private int BookID;
    private String OutDate;





    private List<User> users;




    private List<Book> books;


    public BookBorrow(
        None UserCode,        String InDate,        int BorrowID,        int BookID,        String OutDate    ) {
        this.UserCode = UserCode;
        this.InDate = InDate;
        this.BorrowID = BorrowID;
        this.BookID = BookID;
        this.OutDate = OutDate;
        this.users = new ArrayList<>();
        this.books = new ArrayList<>();
    }

    public BookBorrow(
        None UserCode,        String InDate,        int BorrowID,        int BookID,        String OutDate        ArrayList<User> users,        ArrayList<Book> books    ) {
        this.UserCode = UserCode;
        this.InDate = InDate;
        this.BorrowID = BorrowID;
        this.BookID = BookID;
        this.OutDate = OutDate;
        this.users = users;
        this.books = books;
    }

    public None getUsercode() {
        return UserCode;
    }

    public void setUsercode(None UserCode) {
        this.UserCode = UserCode;
    }
    public String getIndate() {
        return InDate;
    }

    public void setIndate(String InDate) {
        this.InDate = InDate;
    }
    public int getBorrowid() {
        return BorrowID;
    }

    public void setBorrowid(int BorrowID) {
        this.BorrowID = BorrowID;
    }
    public int getBookid() {
        return BookID;
    }

    public void setBookid(int BookID) {
        this.BookID = BookID;
    }
    public String getOutdate() {
        return OutDate;
    }

    public void setOutdate(String OutDate) {
        this.OutDate = OutDate;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }
    public List<Book> getBooks() {
        return books;
    }

    public void addBook(Book book) {
        this.books.add(book);
    }

}