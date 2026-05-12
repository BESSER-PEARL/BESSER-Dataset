





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String email;
    private String username;
    private int CustomerID;





    private Book book;




    private Customer customer;




    private Administrator administrator;




    private List<Book> books;


    public Customer(
        String email,        String username,        int CustomerID    ) {
        this.email = email;
        this.username = username;
        this.CustomerID = CustomerID;
        this.books = new ArrayList<>();
    }

    public Customer(
        String email,        String username,        int CustomerID        ArrayList<Book> books    ) {
        this.email = email;
        this.username = username;
        this.CustomerID = CustomerID;
        this.books = books;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public int getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(int CustomerID) {
        this.CustomerID = CustomerID;
    }

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public List<Book> getBooks() {
        return books;
    }

    public void addBook(Book book) {
        this.books.add(book);
    }

}