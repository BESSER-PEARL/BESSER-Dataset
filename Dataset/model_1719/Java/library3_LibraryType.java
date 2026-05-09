





import java.util.List;
import java.util.ArrayList;

public class library3_LibraryType  {






    private library3_DocumentRoot library3_documentroot;




    private List<library3_BookType> library3_booktypes;




    private List<library3_CustomerType> library3_customertypes;


    public library3_LibraryType(
    ) {
        this.library3_booktypes = new ArrayList<>();
        this.library3_customertypes = new ArrayList<>();
    }

    public library3_LibraryType(
        ArrayList<library3_BookType> library3_booktypes,        ArrayList<library3_CustomerType> library3_customertypes    ) {
        this.library3_booktypes = library3_booktypes;
        this.library3_customertypes = library3_customertypes;
    }


    public library3_DocumentRoot getLibrary3_documentroot() {
        return library3_documentroot;
    }

    public void setLibrary3_documentroot(library3_DocumentRoot library3_documentroot) {
        this.library3_documentroot = library3_documentroot;
    }
    public List<library3_BookType> getLibrary3_booktypes() {
        return library3_booktypes;
    }

    public void addLibrary3_booktype(Library3_booktype library3_booktype) {
        this.library3_booktypes.add(library3_booktype);
    }
    public List<library3_CustomerType> getLibrary3_customertypes() {
        return library3_customertypes;
    }

    public void addLibrary3_customertype(Library3_customertype library3_customertype) {
        this.library3_customertypes.add(library3_customertype);
    }

}