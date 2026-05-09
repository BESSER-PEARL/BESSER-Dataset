





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_BooleanLiteral extends Literal {

    private String value;



    public kermeta_behavior_BooleanLiteral(
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