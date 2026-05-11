





import java.util.List;
import java.util.ArrayList;

public class actionpak1_InvokeSaflet2 extends ParameterizedActionstep {

    private String labelText;





    private DynamicValue dynamicvalue;


    public actionpak1_InvokeSaflet2(
        String labelText    ) {
        super(
        );
        this.labelText = labelText;
    }


    public String getLabeltext() {
        return labelText;
    }

    public void setLabeltext(String labelText) {
        this.labelText = labelText;
    }

    public DynamicValue getDynamicvalue() {
        return dynamicvalue;
    }

    public void setDynamicvalue(DynamicValue dynamicvalue) {
        this.dynamicvalue = dynamicvalue;
    }

}