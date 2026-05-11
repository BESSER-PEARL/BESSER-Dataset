





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Literal extends Expression {

    private String value;
    private String type;



    public JavaSimplified_Literal(
        String value,        String type    ) {
        super(
        );
        this.value = value;
        this.type = type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}