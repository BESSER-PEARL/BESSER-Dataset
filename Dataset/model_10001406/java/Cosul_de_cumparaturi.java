




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Cosul_de_cumparaturi  {

    private LocalDate creationDate;



    public Cosul_de_cumparaturi(
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