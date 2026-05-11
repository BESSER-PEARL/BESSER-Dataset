





import java.util.List;
import java.util.ArrayList;

public class automata_StringVariable extends Variable {

    private String initialValue;
    private String value;



    public automata_StringVariable(
        String initialValue,        String value    ) {
        super(
        );
        this.initialValue = initialValue;
        this.value = value;
    }


    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}