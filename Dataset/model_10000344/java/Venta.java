




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Venta  {

    private LocalDate creationDate;



    public Venta(
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