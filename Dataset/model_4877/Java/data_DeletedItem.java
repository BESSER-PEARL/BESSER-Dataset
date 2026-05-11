




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_DeletedItem extends Item {

    private String identOfDeleted;
    private LocalDate deleted;



    public data_DeletedItem(
        String identOfDeleted,        LocalDate deleted    ) {
        super(
        );
        this.identOfDeleted = identOfDeleted;
        this.deleted = deleted;
    }


    public String getIdentofdeleted() {
        return identOfDeleted;
    }

    public void setIdentofdeleted(String identOfDeleted) {
        this.identOfDeleted = identOfDeleted;
    }
    public LocalDate getDeleted() {
        return deleted;
    }

    public void setDeleted(LocalDate deleted) {
        this.deleted = deleted;
    }


}