





import java.util.List;
import java.util.ArrayList;

public class esper_TerminalExpression  {

    private boolean parenthesis;
    private boolean every;





    private esper_FollowBy esper_followby;




    private esper_FollowBy esper_followby;




    private esper_FollowBy esper_followby;




    private esper_SingleDefinition esper_singledefinition;




    private esper_FollowBy esper_followby;


    public esper_TerminalExpression(
        boolean parenthesis,        boolean every    ) {
        this.parenthesis = parenthesis;
        this.every = every;
    }


    public boolean getParenthesis() {
        return parenthesis;
    }

    public void setParenthesis(boolean parenthesis) {
        this.parenthesis = parenthesis;
    }
    public boolean getEvery() {
        return every;
    }

    public void setEvery(boolean every) {
        this.every = every;
    }

    public esper_FollowBy getEsper_followby() {
        return esper_followby;
    }

    public void setEsper_followby(esper_FollowBy esper_followby) {
        this.esper_followby = esper_followby;
    }
    public esper_FollowBy getEsper_followby() {
        return esper_followby;
    }

    public void setEsper_followby(esper_FollowBy esper_followby) {
        this.esper_followby = esper_followby;
    }
    public esper_FollowBy getEsper_followby() {
        return esper_followby;
    }

    public void setEsper_followby(esper_FollowBy esper_followby) {
        this.esper_followby = esper_followby;
    }
    public esper_SingleDefinition getEsper_singledefinition() {
        return esper_singledefinition;
    }

    public void setEsper_singledefinition(esper_SingleDefinition esper_singledefinition) {
        this.esper_singledefinition = esper_singledefinition;
    }
    public esper_FollowBy getEsper_followby() {
        return esper_followby;
    }

    public void setEsper_followby(esper_FollowBy esper_followby) {
        this.esper_followby = esper_followby;
    }

}