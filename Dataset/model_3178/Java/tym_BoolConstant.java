





import java.util.List;
import java.util.ArrayList;

public class tym_BoolConstant extends Expression {

    private String value;



    public tym_BoolConstant(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}