





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int CustomerID;
    private String email;
    private String username;





    private Book book;




    private Customer customer;




    private List<Book> books;




    private Administrator administrator;


    public Customer(
        int CustomerID,        String email,        String username    ) {
        this.CustomerID = CustomerID;
        this.email = email;
        this.username = username;
        this.books = new ArrayList<>();
    }

    public Customer(
        int CustomerID,        String email,        String username        ArrayList<Book> books    ) {
        this.CustomerID = CustomerID;
        this.email = email;
        this.username = username;
        this.books = books;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
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