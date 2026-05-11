




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class training_Session  {

    private LocalDate date;
    private String name;



    public training_Session(
        LocalDate date,        String name    ) {
        this.date = date;
        this.name = name;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}