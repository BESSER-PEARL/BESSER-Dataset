





import java.util.List;
import java.util.ArrayList;

public class fenix_LessonPeriod  {

    private String end;
    private String start;





    private fenix_Shift fenix_shift;


    public fenix_LessonPeriod(
        String end,        String start    ) {
        this.end = end;
        this.start = start;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public fenix_Shift getFenix_shift() {
        return fenix_shift;
    }

    public void setFenix_shift(fenix_Shift fenix_shift) {
        this.fenix_shift = fenix_shift;
    }

}