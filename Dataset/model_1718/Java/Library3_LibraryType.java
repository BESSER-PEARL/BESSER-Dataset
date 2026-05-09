





import java.util.List;
import java.util.ArrayList;

public class Library3_LibraryType  {






    private Library3_DocumentRoot library3_documentroot;




    private List<Library3_BookType> library3_booktypes;




    private List<Library3_CustomerType> library3_customertypes;


    public Library3_LibraryType(
    ) {
        this.library3_booktypes = new ArrayList<>();
        this.library3_customertypes = new ArrayList<>();
    }

    public Library3_LibraryType(
        ArrayList<Library3_BookType> library3_booktypes,        ArrayList<Library3_CustomerType> library3_customertypes    ) {
        this.library3_booktypes = library3_booktypes;
        this.library3_customertypes = library3_customertypes;
    }


    public Library3_DocumentRoot getLibrary3_documentroot() {
        return library3_documentroot;
    }

    public void setLibrary3_documentroot(Library3_DocumentRoot library3_documentroot) {
        this.library3_documentroot = library3_documentroot;
    }
    public List<Library3_BookType> getLibrary3_booktypes() {
        return library3_booktypes;
    }

    public void addLibrary3_booktype(Library3_booktype library3_booktype) {
        this.library3_booktypes.add(library3_booktype);
    }
    public List<Library3_CustomerType> getLibrary3_customertypes() {
        return library3_customertypes;
    }

    public void addLibrary3_customertype(Library3_customertype library3_customertype) {
        this.library3_customertypes.add(library3_customertype);
    }

}