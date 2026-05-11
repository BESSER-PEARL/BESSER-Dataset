





import java.util.List;
import java.util.ArrayList;

public class siddhi_QueryOutput extends DELETE, FOR, INTO, UPDATE, RETURN, INSERT {






    private siddhi_Query siddhi_query;




    private siddhi_OutputEventType siddhi_outputeventtype;


    public siddhi_QueryOutput(
    ) {
        super(
        );
    }



    public siddhi_Query getSiddhi_query() {
        return siddhi_query;
    }

    public void setSiddhi_query(siddhi_Query siddhi_query) {
        this.siddhi_query = siddhi_query;
    }
    public siddhi_OutputEventType getSiddhi_outputeventtype() {
        return siddhi_outputeventtype;
    }

    public void setSiddhi_outputeventtype(siddhi_OutputEventType siddhi_outputeventtype) {
        this.siddhi_outputeventtype = siddhi_outputeventtype;
    }

}