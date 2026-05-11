





import java.util.List;
import java.util.ArrayList;

public class siddhi_OutputRate extends OUTPUT, SNAPSHOT, EVENTS {






    private siddhi_EVERY siddhi_every;




    private siddhi_AnonymousStream siddhi_anonymousstream;




    private siddhi_Query siddhi_query;




    private siddhi_TimeValue siddhi_timevalue;


    public siddhi_OutputRate(
    ) {
        super(
        );
    }



    public siddhi_EVERY getSiddhi_every() {
        return siddhi_every;
    }

    public void setSiddhi_every(siddhi_EVERY siddhi_every) {
        this.siddhi_every = siddhi_every;
    }
    public siddhi_AnonymousStream getSiddhi_anonymousstream() {
        return siddhi_anonymousstream;
    }

    public void setSiddhi_anonymousstream(siddhi_AnonymousStream siddhi_anonymousstream) {
        this.siddhi_anonymousstream = siddhi_anonymousstream;
    }
    public siddhi_Query getSiddhi_query() {
        return siddhi_query;
    }

    public void setSiddhi_query(siddhi_Query siddhi_query) {
        this.siddhi_query = siddhi_query;
    }
    public siddhi_TimeValue getSiddhi_timevalue() {
        return siddhi_timevalue;
    }

    public void setSiddhi_timevalue(siddhi_TimeValue siddhi_timevalue) {
        this.siddhi_timevalue = siddhi_timevalue;
    }

}