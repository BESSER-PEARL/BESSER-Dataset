





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_InputItem extends CaseItem {

    private String parameterName;
    private boolean required;



    public core_actionstep_InputItem(
        String parameterName,        boolean required    ) {
        super(
        );
        this.parameterName = parameterName;
        this.required = required;
    }


    public String getParametername() {
        return parameterName;
    }

    public void setParametername(String parameterName) {
        this.parameterName = parameterName;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }


}