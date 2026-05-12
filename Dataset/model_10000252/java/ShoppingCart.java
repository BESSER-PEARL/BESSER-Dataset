




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private LocalDate creationDate;
    private int id;



    public ShoppingCart(
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