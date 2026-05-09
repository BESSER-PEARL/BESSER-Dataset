




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class extlibrary_Item  {

    private LocalDate publicationDate;



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


}