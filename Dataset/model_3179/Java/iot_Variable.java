





import java.util.List;
import java.util.ArrayList;

public class iot_Variable extends AbstractElement {

    private String name;





    private iot_VariableRef iot_variableref;


    public iot_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iot_VariableRef getIot_variableref() {
        return iot_variableref;
    }

    public void setIot_variableref(iot_VariableRef iot_variableref) {
        this.iot_variableref = iot_variableref;
    }

}