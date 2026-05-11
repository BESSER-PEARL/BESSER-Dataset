





import java.util.List;
import java.util.ArrayList;

public class transformationtrace_RuleParameterTrace  {

    private String parameterName;
    private String objectId;



    public transformationtrace_RuleParameterTrace(
        String parameterName,        String objectId    ) {
        this.parameterName = parameterName;
        this.objectId = objectId;
    }


    public String getParametername() {
        return parameterName;
    }

    public void setParametername(String parameterName) {
        this.parameterName = parameterName;
    }
    public String getObjectid() {
        return objectId;
    }

    public void setObjectid(String objectId) {
        this.objectId = objectId;
    }


}