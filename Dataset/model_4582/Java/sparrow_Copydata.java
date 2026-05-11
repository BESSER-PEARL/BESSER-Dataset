





import java.util.List;
import java.util.ArrayList;

public class sparrow_Copydata extends Action {

    private String value;
    private String source;
    private String to;



    public sparrow_Copydata(
        String value,        String source,        String to    ) {
        super(
        );
        this.value = value;
        this.source = source;
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
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }


}