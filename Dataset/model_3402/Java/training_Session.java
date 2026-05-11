




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class training_Session  {

    private LocalDate date;



    public training_Session(
        LocalDate date    ) {
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}