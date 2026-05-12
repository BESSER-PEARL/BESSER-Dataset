




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingBAsket  {

    private LocalDate creationDate;
    private int id;



    public ShoppingBAsket(
        LocalDate creationDate,        int id    ) {
        this.creationDate = creationDate;
        this.id = id;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}