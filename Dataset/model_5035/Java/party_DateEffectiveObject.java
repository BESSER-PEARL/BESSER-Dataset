




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class party_DateEffectiveObject extends Tagged {

    private LocalDate start;
    private LocalDate end;



    public party_DateEffectiveObject(
        LocalDate start,        LocalDate end    ) {
        super(
        );
        this.start = start;
        this.end = end;
    }


    public LocalDate getStart() {
        return start;
    }

    public void setStart(LocalDate start) {
        this.start = start;
    }
    public LocalDate getEnd() {
        return end;
    }

    public void setEnd(LocalDate end) {
        this.end = end;
    }


}