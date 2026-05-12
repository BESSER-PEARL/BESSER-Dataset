





import java.util.List;
import java.util.ArrayList;

public class transaction  {






    private library_member library_member;




    private book book;




    private fine fine;




    private List<librarian> librarians;


    public transaction(
    ) {
        this.librarians = new ArrayList<>();
    }

    public transaction(
        ArrayList<librarian> librarians    ) {
        this.librarians = librarians;
    }


    public library_member getLibrary_member() {
        return library_member;
    }

    public void setLibrary_member(library_member library_member) {
        this.library_member = library_member;
    }
    public book getBook() {
        return book;
    }

    public void setBook(book book) {
        this.book = book;
    }
    public fine getFine() {
        return fine;
    }

    public void setFine(fine fine) {
        this.fine = fine;
    }
    public List<librarian> getLibrarians() {
        return librarians;
    }

    public void addLibrarian(Librarian librarian) {
        this.librarians.add(librarian);
    }

}