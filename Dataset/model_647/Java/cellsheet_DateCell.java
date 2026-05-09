




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class cellsheet_DateCell extends Cell {

    private LocalDate value;



    public cellsheet_DateCell(
        LocalDate value    ) {
        super(
        );
        this.value = value;
    }


    public LocalDate getValue() {
        return value;
    }

    public void setValue(LocalDate value) {
        this.value = value;
    }


}