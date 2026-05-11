





import java.util.List;
import java.util.ArrayList;

public class dsl_Fetch extends Action {

    private String source;
    private String value;



    public dsl_Fetch(
        String source,        String value    ) {
        super(
        );
        this.source = source;
        this.value = value;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}