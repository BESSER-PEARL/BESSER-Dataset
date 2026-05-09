




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class publication103_Review extends Labelled {

    private LocalDate date;



    public publication103_Review(
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