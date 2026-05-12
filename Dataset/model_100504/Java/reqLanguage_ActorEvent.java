





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_ActorEvent  {

    private String action;





    private reqLanguage_EObject reqlanguage_eobject;


    public reqLanguage_ActorEvent(
        String action    ) {
        this.action = action;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public reqLanguage_EObject getReqlanguage_eobject() {
        return reqlanguage_eobject;
    }

    public void setReqlanguage_eobject(reqLanguage_EObject reqlanguage_eobject) {
        this.reqlanguage_eobject = reqlanguage_eobject;
    }

}