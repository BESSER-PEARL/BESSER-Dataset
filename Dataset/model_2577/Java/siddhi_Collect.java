





import java.util.List;
import java.util.ArrayList;

public class siddhi_Collect  {

    private String end;
    private String start;





    private siddhi_StandardStatefulSource siddhi_standardstatefulsource;


    public siddhi_Collect(
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

    public siddhi_StandardStatefulSource getSiddhi_standardstatefulsource() {
        return siddhi_standardstatefulsource;
    }

    public void setSiddhi_standardstatefulsource(siddhi_StandardStatefulSource siddhi_standardstatefulsource) {
        this.siddhi_standardstatefulsource = siddhi_standardstatefulsource;
    }

}