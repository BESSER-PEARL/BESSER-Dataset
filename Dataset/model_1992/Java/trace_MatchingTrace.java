





import java.util.List;
import java.util.ArrayList;

public class trace_MatchingTrace extends AbstractTrace {

    private String queryText;



    public trace_MatchingTrace(
        String queryText    ) {
        super(
        );
        this.queryText = queryText;
    }


    public String getQuerytext() {
        return queryText;
    }

    public void setQuerytext(String queryText) {
        this.queryText = queryText;
    }


}