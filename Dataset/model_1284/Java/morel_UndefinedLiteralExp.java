





import java.util.List;
import java.util.ArrayList;

public class morel_UndefinedLiteralExp extends LiteralExp {

    private String value;



    public morel_UndefinedLiteralExp(
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