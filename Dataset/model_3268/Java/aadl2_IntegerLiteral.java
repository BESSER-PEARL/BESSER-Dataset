





import java.util.List;
import java.util.ArrayList;

public class aadl2_IntegerLiteral extends NumberValue {

    private String value;
    private String base;



    public aadl2_IntegerLiteral(
        String value,        String base    ) {
        super(
        );
        this.value = value;
        this.base = base;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getBase() {
        return base;
    }

    public void setBase(String base) {
        this.base = base;
    }


}