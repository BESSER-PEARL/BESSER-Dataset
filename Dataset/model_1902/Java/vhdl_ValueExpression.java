





import java.util.List;
import java.util.ArrayList;

public class vhdl_ValueExpression  {

    private String value;





    private vhdl_Value vhdl_value;


    public vhdl_ValueExpression(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vhdl_Value getVhdl_value() {
        return vhdl_value;
    }

    public void setVhdl_value(vhdl_Value vhdl_value) {
        this.vhdl_value = vhdl_value;
    }

}