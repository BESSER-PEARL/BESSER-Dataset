





import java.util.List;
import java.util.ArrayList;

public class libraryModel_ecore_LibraryModel  {






    private List<libraryModel_ecore_Book> librarymodel_ecore_books;




    private libraryModel_ecore_Book librarymodel_ecore_book;




    private List<libraryModel_ecore_Author> librarymodel_ecore_authors;




    private libraryModel_ecore_Author librarymodel_ecore_author;


    public libraryModel_ecore_LibraryModel(
    ) {
        this.librarymodel_ecore_books = new ArrayList<>();
        this.librarymodel_ecore_authors = new ArrayList<>();
    }

    public libraryModel_ecore_LibraryModel(
        ArrayList<libraryModel_ecore_Book> librarymodel_ecore_books,        ArrayList<libraryModel_ecore_Author> librarymodel_ecore_authors    ) {
        this.librarymodel_ecore_books = librarymodel_ecore_books;
        this.librarymodel_ecore_authors = librarymodel_ecore_authors;
    }


    public List<libraryModel_ecore_Book> getLibrarymodel_ecore_books() {
        return librarymodel_ecore_books;
    }

    public void addLibrarymodel_ecore_book(Librarymodel_ecore_book librarymodel_ecore_book) {
        this.librarymodel_ecore_books.add(librarymodel_ecore_book);
    }
    public libraryModel_ecore_Book getLibrarymodel_ecore_book() {
        return librarymodel_ecore_book;
    }

    public void setLibrarymodel_ecore_book(libraryModel_ecore_Book librarymodel_ecore_book) {
        this.librarymodel_ecore_book = librarymodel_ecore_book;
    }
    public List<libraryModel_ecore_Author> getLibrarymodel_ecore_authors() {
        return librarymodel_ecore_authors;
    }

    public void addLibrarymodel_ecore_author(Librarymodel_ecore_author librarymodel_ecore_author) {
        this.librarymodel_ecore_authors.add(librarymodel_ecore_author);
    }
    public libraryModel_ecore_Author getLibrarymodel_ecore_author() {
        return librarymodel_ecore_author;
    }

    public void setLibrarymodel_ecore_author(libraryModel_ecore_Author librarymodel_ecore_author) {
        this.librarymodel_ecore_author = librarymodel_ecore_author;
    }

}