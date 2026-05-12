




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tp4_Review extends Labelled {

    private LocalDate date;



    public tp4_Review(
        LocalDate date    ) {
        super(
        );
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}