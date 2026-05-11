





import java.util.List;
import java.util.ArrayList;

public class express_VarLiteral extends IndexTerminal {

    private String value;



    public express_VarLiteral(
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