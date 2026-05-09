





import java.util.List;
import java.util.ArrayList;

public class library_BookCopy  {

    private int copies;





    private library_Library library_library;


    public library_BookCopy(
        int copies    ) {
        this.copies = copies;
    }


    public int getCopies() {
        return copies;
    }

    public void setCopies(int copies) {
        this.copies = copies;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}