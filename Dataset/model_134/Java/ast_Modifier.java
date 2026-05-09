





import java.util.List;
import java.util.ArrayList;

public class ast_Modifier extends EJElement {

    private String value;



    public ast_Modifier(
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