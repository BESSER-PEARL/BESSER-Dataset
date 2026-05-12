





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String username;
    private int CustomerID;
    private String email;





    private Customer customer;




    private Book book;




    private List<Book> books;




    private Administrator administrator;


    public Customer(
        String username,        int CustomerID,        String email    ) {
        this.username = username;
        this.CustomerID = CustomerID;
        this.email = email;
        this.books = new ArrayList<>();
    }

    public Customer(
        String username,        int CustomerID,        String email        ArrayList<Book> books    ) {
        this.username = username;
        this.CustomerID = CustomerID;
        this.email = email;
        this.books = books;
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
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
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
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}