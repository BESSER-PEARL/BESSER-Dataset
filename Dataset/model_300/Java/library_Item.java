




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class library_Item  {

    private LocalDate publicationDate;



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


}