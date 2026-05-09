




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Library_Item  {

    private LocalDate publicationDate;





    private Library_Library library_library;


    public Library_Item(
        LocalDate publicationDate    ) {
        this.publicationDate = publicationDate;
    }


    public LocalDate getPublicationdate() {
        return publicationDate;
    }

    public void setPublicationdate(LocalDate publicationDate) {
        this.publicationDate = publicationDate;
    }

    public Library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(Library_Library library_library) {
        this.library_library = library_library;
    }

}