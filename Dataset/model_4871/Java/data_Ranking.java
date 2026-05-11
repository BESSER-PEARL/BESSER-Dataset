




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_Ranking extends Extension {

    private LocalDate date;



    public data_Ranking(
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