





import java.util.List;
import java.util.ArrayList;

public class aadl2_IntegerLiteral extends NumberValue {

    private String base;
    private String value;



    public aadl2_IntegerLiteral(
        String base,        String value    ) {
        super(
        );
        this.base = base;
        this.value = value;
    }


    public String getBase() {
        return base;
    }

    public void setBase(String base) {
        this.base = base;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}