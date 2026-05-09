





import java.util.List;
import java.util.ArrayList;

public class vhdl_Open extends Expression {

    private String value;



    public vhdl_Open(
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