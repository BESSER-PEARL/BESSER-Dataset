





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_Parameter extends NamedElement {






    private Value value;


    public SQLDDL_Parameter(
    ) {
        super(
        );
    }



    public Value getValue() {
        return value;
    }

    public void setValue(Value value) {
        this.value = value;
    }

}