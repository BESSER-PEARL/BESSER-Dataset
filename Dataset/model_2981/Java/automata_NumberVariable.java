





import java.util.List;
import java.util.ArrayList;

public class automata_NumberVariable extends Variable {

    private String initialValue;



    public automata_NumberVariable(
        String initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
    }


    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }


}