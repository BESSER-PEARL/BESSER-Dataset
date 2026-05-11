




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_DeletedItem extends Item {

    private LocalDate deleted;
    private String identOfDeleted;



    public data_DeletedItem(
        LocalDate deleted,        String identOfDeleted    ) {
        super(
        );
        this.deleted = deleted;
        this.identOfDeleted = identOfDeleted;
    }


    public LocalDate getDeleted() {
        return deleted;
    }

    public void setDeleted(LocalDate deleted) {
        this.deleted = deleted;
    }
    public String getIdentofdeleted() {
        return identOfDeleted;
    }

    public void setIdentofdeleted(String identOfDeleted) {
        this.identOfDeleted = identOfDeleted;
    }


}