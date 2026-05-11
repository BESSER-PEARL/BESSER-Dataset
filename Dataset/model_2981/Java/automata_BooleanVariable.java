





import java.util.List;
import java.util.ArrayList;

public class automata_BooleanVariable extends Variable {

    private boolean initialValue;



    public automata_BooleanVariable(
        boolean initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
    }


    public boolean getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(boolean initialValue) {
        this.initialValue = initialValue;
    }


}