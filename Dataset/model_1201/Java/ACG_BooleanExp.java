





import java.util.List;
import java.util.ArrayList;

public class ACG_BooleanExp extends LiteralExp {

    private String value;



    public ACG_BooleanExp(
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