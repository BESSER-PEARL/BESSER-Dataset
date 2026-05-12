





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_Condition  {

    private String script;





    private scxmlxt_AbstractTransition scxmlxt_abstracttransition;


    public scxmlxt_Condition(
        String script    ) {
        this.script = script;
    }


    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }

    public scxmlxt_AbstractTransition getScxmlxt_abstracttransition() {
        return scxmlxt_abstracttransition;
    }

    public void setScxmlxt_abstracttransition(scxmlxt_AbstractTransition scxmlxt_abstracttransition) {
        this.scxmlxt_abstracttransition = scxmlxt_abstracttransition;
    }

}