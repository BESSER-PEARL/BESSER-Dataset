





import java.util.List;
import java.util.ArrayList;

public class SecCon_Rule  {

    private boolean logicValue;
    private String operator;
    private String name;





    private SecCon_ContextScenario seccon_contextscenario;


    public SecCon_Rule(
        boolean logicValue,        String operator,        String name    ) {
        this.logicValue = logicValue;
        this.operator = operator;
        this.name = name;
    }


    public boolean getLogicvalue() {
        return logicValue;
    }

    public void setLogicvalue(boolean logicValue) {
        this.logicValue = logicValue;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SecCon_ContextScenario getSeccon_contextscenario() {
        return seccon_contextscenario;
    }

    public void setSeccon_contextscenario(SecCon_ContextScenario seccon_contextscenario) {
        this.seccon_contextscenario = seccon_contextscenario;
    }

}