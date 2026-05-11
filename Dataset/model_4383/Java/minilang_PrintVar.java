





import java.util.List;
import java.util.ArrayList;

public class minilang_PrintVar extends Statement {

    private String value;



    public minilang_PrintVar(
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