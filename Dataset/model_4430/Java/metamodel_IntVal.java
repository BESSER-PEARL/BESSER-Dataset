





import java.util.List;
import java.util.ArrayList;

public class metamodel_IntVal extends Type {

    private int value;



    public metamodel_IntVal(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}