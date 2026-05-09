





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Books  {






    private libraryinteractionmodel_Library libraryinteractionmodel_library;




    private List<libraryinteractionmodel_BookShort> libraryinteractionmodel_bookshorts;


    public libraryinteractionmodel_Books(
    ) {
        this.libraryinteractionmodel_bookshorts = new ArrayList<>();
    }

    public libraryinteractionmodel_Books(
        ArrayList<libraryinteractionmodel_BookShort> libraryinteractionmodel_bookshorts    ) {
        this.libraryinteractionmodel_bookshorts = libraryinteractionmodel_bookshorts;
    }


    public libraryinteractionmodel_Library getLibraryinteractionmodel_library() {
        return libraryinteractionmodel_library;
    }

    public void setLibraryinteractionmodel_library(libraryinteractionmodel_Library libraryinteractionmodel_library) {
        this.libraryinteractionmodel_library = libraryinteractionmodel_library;
    }
    public List<libraryinteractionmodel_BookShort> getLibraryinteractionmodel_bookshorts() {
        return libraryinteractionmodel_bookshorts;
    }

    public void addLibraryinteractionmodel_bookshort(Libraryinteractionmodel_bookshort libraryinteractionmodel_bookshort) {
        this.libraryinteractionmodel_bookshorts.add(libraryinteractionmodel_bookshort);
    }

}