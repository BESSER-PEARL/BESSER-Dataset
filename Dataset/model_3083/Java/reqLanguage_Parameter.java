





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Parameter  {

    private String name;
    private String parameter;





    private reqLanguage_ActorEvent reqlanguage_actorevent;


    public reqLanguage_Parameter(
        String name,        String parameter    ) {
        this.name = name;
        this.parameter = parameter;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }

    public reqLanguage_ActorEvent getReqlanguage_actorevent() {
        return reqlanguage_actorevent;
    }

    public void setReqlanguage_actorevent(reqLanguage_ActorEvent reqlanguage_actorevent) {
        this.reqlanguage_actorevent = reqlanguage_actorevent;
    }

}