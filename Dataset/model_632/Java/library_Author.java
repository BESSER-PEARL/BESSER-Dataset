





import java.util.List;
import java.util.ArrayList;

public class library_Author extends AbstractPerson {






    private library_UoD library_uod;




    private library_Book library_book;


    public library_Author(
    ) {
        super(
        );
    }



    public library_UoD getLibrary_uod() {
        return library_uod;
    }

    public void setLibrary_uod(library_UoD library_uod) {
        this.library_uod = library_uod;
    }
    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }

}