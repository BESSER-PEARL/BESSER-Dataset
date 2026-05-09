




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class extlibrary_Item  {

    private LocalDate publicationDate;





    private extlibrary_Library extlibrary_library;


    public extlibrary_Item(
        LocalDate publicationDate    ) {
        this.publicationDate = publicationDate;
    }


    public LocalDate getPublicationdate() {
        return publicationDate;
    }

    public void setPublicationdate(LocalDate publicationDate) {
        this.publicationDate = publicationDate;
    }

    public extlibrary_Library getExtlibrary_library() {
        return extlibrary_library;
    }

    public void setExtlibrary_library(extlibrary_Library extlibrary_library) {
        this.extlibrary_library = extlibrary_library;
    }

}