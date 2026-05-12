





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String username;
    private String email;
    private int CustomerID;





    private Customer customer;




    private Administrator administrator;




    private Book book;




    private List<Book> books;


    public Customer(
        String username,        String email,        int CustomerID    ) {
        this.username = username;
        this.email = email;
        this.CustomerID = CustomerID;
        this.books = new ArrayList<>();
    }

    public Customer(
        String username,        String email,        int CustomerID        ArrayList<Book> books    ) {
        this.username = username;
        this.email = email;
        this.CustomerID = CustomerID;
        this.books = books;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(int CustomerID) {
        this.CustomerID = CustomerID;
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
    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }
    public List<Book> getBooks() {
        return books;
    }

    public void addBook(Book book) {
        this.books.add(book);
    }

}