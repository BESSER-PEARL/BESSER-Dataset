




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class AddPost  {

    private LocalDate creationDate;



    public AddPost(
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