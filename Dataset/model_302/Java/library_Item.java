




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class library_Item  {

    private LocalDate publicationDate;





    private library_Library library_library;


    public library_Item(
        LocalDate publicationDate    ) {
        this.publicationDate = publicationDate;
    }


    public LocalDate getPublicationdate() {
        return publicationDate;
    }

    public void setPublicationdate(LocalDate publicationDate) {
        this.publicationDate = publicationDate;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}