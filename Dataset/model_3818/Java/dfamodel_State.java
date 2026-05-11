





import java.util.List;
import java.util.ArrayList;

public class dfamodel_State  {

    private boolean isStart;
    private boolean isEnd;
    private String id;





    private dfamodel_DFA dfamodel_dfa;


    public dfamodel_State(
        boolean isStart,        boolean isEnd,        String id    ) {
        this.isStart = isStart;
        this.isEnd = isEnd;
        this.id = id;
    }


    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }
    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
        this.isEnd = isEnd;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dfamodel_DFA getDfamodel_dfa() {
        return dfamodel_dfa;
    }

    public void setDfamodel_dfa(dfamodel_DFA dfamodel_dfa) {
        this.dfamodel_dfa = dfamodel_dfa;
    }

}