




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Choices  {

    private LocalDate creationDate;



    public Choices(
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