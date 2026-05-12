




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_ShoppingCart  {

    private LocalDate creationDate;



    public ShoppingCartExample_ShoppingCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }


}