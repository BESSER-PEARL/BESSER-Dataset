





import java.util.List;
import java.util.ArrayList;

public class dsl_LoadCsv extends Action {

    private String delim;
    private String source;
    private String to;
    private String value;



    public dsl_LoadCsv(
        String delim,        String source,        String to,        String value    ) {
        super(
        );
        this.delim = delim;
        this.source = source;
        this.to = to;
        this.value = value;
    }


    public String getDelim() {
        return delim;
    }

    public void setDelim(String delim) {
        this.delim = delim;
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
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}