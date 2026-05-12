





import java.util.List;
import java.util.ArrayList;

public class library  {






    private List<transaction> transactions;




    private List<librarian> librarians;




    private List<book> books;


    public library(
    ) {
        this.transactions = new ArrayList<>();
        this.librarians = new ArrayList<>();
        this.books = new ArrayList<>();
    }

    public library(
        ArrayList<transaction> transactions,        ArrayList<librarian> librarians,        ArrayList<book> books    ) {
        this.transactions = transactions;
        this.librarians = librarians;
        this.books = books;
    }


    public List<transaction> getTransactions() {
        return transactions;
    }

    public void addTransaction(Transaction transaction) {
        this.transactions.add(transaction);
    }
    public List<librarian> getLibrarians() {
        return librarians;
    }

    public void addLibrarian(Librarian librarian) {
        this.librarians.add(librarian);
    }
    public List<book> getBooks() {
        return books;
    }

    public void addBook(Book book) {
        this.books.add(book);
    }

}