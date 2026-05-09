





import java.util.List;
import java.util.ArrayList;

public class trace_States_Place_tokens_State  {

    private int tokens;





    private petrinet_TracedPlace petrinet_tracedplace;


    public trace_States_Place_tokens_State(
        int tokens    ) {
        this.tokens = tokens;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }

    public petrinet_TracedPlace getPetrinet_tracedplace() {
        return petrinet_tracedplace;
    }

    public void setPetrinet_tracedplace(petrinet_TracedPlace petrinet_tracedplace) {
        this.petrinet_tracedplace = petrinet_tracedplace;
    }

}