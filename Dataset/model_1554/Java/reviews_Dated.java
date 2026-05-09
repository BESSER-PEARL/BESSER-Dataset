




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class reviews_Dated  {

    private LocalDate creationDate;
    private LocalDate modificationDate;



    public reviews_Dated(
        LocalDate creationDate,        LocalDate modificationDate    ) {
        this.creationDate = creationDate;
        this.modificationDate = modificationDate;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public LocalDate getModificationdate() {
        return modificationDate;
    }

    public void setModificationdate(LocalDate modificationDate) {
        this.modificationDate = modificationDate;
    }


}