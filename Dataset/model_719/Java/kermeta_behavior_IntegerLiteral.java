





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_IntegerLiteral extends Literal {

    private String value;



    public kermeta_behavior_IntegerLiteral(
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