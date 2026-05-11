





import java.util.List;
import java.util.ArrayList;

public class minilang_PrintStr extends Statement {

    private String value;



    public minilang_PrintStr(
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