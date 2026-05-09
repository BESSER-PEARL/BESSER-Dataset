





import java.util.List;
import java.util.ArrayList;

public class ACG_StringExp extends LiteralExp {

    private String value;



    public ACG_StringExp(
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