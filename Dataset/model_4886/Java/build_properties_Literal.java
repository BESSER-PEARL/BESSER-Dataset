





import java.util.List;
import java.util.ArrayList;

public class build_properties_Literal extends IExpr {

    private String value;



    public build_properties_Literal(
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