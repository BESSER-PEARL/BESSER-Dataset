





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_AuthorShort  {

    private String name;
    private String nationality;





    private libraryinteractionmodel_Author libraryinteractionmodel_author;




    private libraryinteractionmodel_Authors libraryinteractionmodel_authors;




    private libraryinteractionmodel_Book libraryinteractionmodel_book;


    public libraryinteractionmodel_AuthorShort(
        String name,        String nationality    ) {
        this.name = name;
        this.nationality = nationality;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }

    public libraryinteractionmodel_Author getLibraryinteractionmodel_author() {
        return libraryinteractionmodel_author;
    }

    public void setLibraryinteractionmodel_author(libraryinteractionmodel_Author libraryinteractionmodel_author) {
        this.libraryinteractionmodel_author = libraryinteractionmodel_author;
    }
    public libraryinteractionmodel_Authors getLibraryinteractionmodel_authors() {
        return libraryinteractionmodel_authors;
    }

    public void setLibraryinteractionmodel_authors(libraryinteractionmodel_Authors libraryinteractionmodel_authors) {
        this.libraryinteractionmodel_authors = libraryinteractionmodel_authors;
    }
    public libraryinteractionmodel_Book getLibraryinteractionmodel_book() {
        return libraryinteractionmodel_book;
    }

    public void setLibraryinteractionmodel_book(libraryinteractionmodel_Book libraryinteractionmodel_book) {
        this.libraryinteractionmodel_book = libraryinteractionmodel_book;
    }

}