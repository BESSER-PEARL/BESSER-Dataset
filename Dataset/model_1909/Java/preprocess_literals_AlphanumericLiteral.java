





import java.util.List;
import java.util.ArrayList;

public class preprocess_literals_AlphanumericLiteral extends Literal {

    private String value;



    public preprocess_literals_AlphanumericLiteral(
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