





import java.util.List;
import java.util.ArrayList;

public class SecCon_Condition  {

    private String condition;
    private String value;
    private boolean logicValue;





    private SecCon_Rule seccon_rule;




    private SecCon_ContextInformation seccon_contextinformation;


    public SecCon_Condition(
        String condition,        String value,        boolean logicValue    ) {
        this.condition = condition;
        this.value = value;
        this.logicValue = logicValue;
    }


    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getLogicvalue() {
        return logicValue;
    }

    public void setLogicvalue(boolean logicValue) {
        this.logicValue = logicValue;
    }

    public SecCon_Rule getSeccon_rule() {
        return seccon_rule;
    }

    public void setSeccon_rule(SecCon_Rule seccon_rule) {
        this.seccon_rule = seccon_rule;
    }
    public SecCon_ContextInformation getSeccon_contextinformation() {
        return seccon_contextinformation;
    }

    public void setSeccon_contextinformation(SecCon_ContextInformation seccon_contextinformation) {
        this.seccon_contextinformation = seccon_contextinformation;
    }

}