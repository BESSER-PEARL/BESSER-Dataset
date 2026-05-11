





import java.util.List;
import java.util.ArrayList;

public class dsl_Copydata extends Action {

    private String to;
    private String value;
    private String source;



    public dsl_Copydata(
        String to,        String value,        String source    ) {
        super(
        );
        this.to = to;
        this.value = value;
        this.source = source;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }


}