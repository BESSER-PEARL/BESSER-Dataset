





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_AuthorShort  {

    private String name;
    private String nationality;





    private libraryinteractionmodel_Book libraryinteractionmodel_book;




    private libraryinteractionmodel_Authors libraryinteractionmodel_authors;


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

    public libraryinteractionmodel_Book getLibraryinteractionmodel_book() {
        return libraryinteractionmodel_book;
    }

    public void setLibraryinteractionmodel_book(libraryinteractionmodel_Book libraryinteractionmodel_book) {
        this.libraryinteractionmodel_book = libraryinteractionmodel_book;
    }
    public libraryinteractionmodel_Authors getLibraryinteractionmodel_authors() {
        return libraryinteractionmodel_authors;
    }

    public void setLibraryinteractionmodel_authors(libraryinteractionmodel_Authors libraryinteractionmodel_authors) {
        this.libraryinteractionmodel_authors = libraryinteractionmodel_authors;
    }

}