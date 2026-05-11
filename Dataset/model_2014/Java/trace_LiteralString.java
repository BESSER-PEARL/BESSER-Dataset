





import java.util.List;
import java.util.ArrayList;

public class trace_LiteralString extends LiteralValue {

    private String stringvalue;



    public trace_LiteralString(
        String stringvalue    ) {
        super(
        );
        this.stringvalue = stringvalue;
    }


    public String getStringvalue() {
        return stringvalue;
    }

    public void setStringvalue(String stringvalue) {
        this.stringvalue = stringvalue;
    }


}