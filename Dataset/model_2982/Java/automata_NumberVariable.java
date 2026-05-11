





import java.util.List;
import java.util.ArrayList;

public class automata_NumberVariable extends Variable {

    private String value;
    private String initialValue;



    public automata_NumberVariable(
        String value,        String initialValue    ) {
        super(
        );
        this.value = value;
        this.initialValue = initialValue;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }


}