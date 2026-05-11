





import java.util.List;
import java.util.ArrayList;

public class b_ValueExpr  {

    private String value;





    private b_Values b_values;


    public b_ValueExpr(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public b_Values getB_values() {
        return b_values;
    }

    public void setB_values(b_Values b_values) {
        this.b_values = b_values;
    }

}