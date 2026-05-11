





import java.util.List;
import java.util.ArrayList;

public class dsl_WriteCsv extends Action {

    private String to;
    private String value;
    private String delim;
    private String source;



    public dsl_WriteCsv(
        String to,        String value,        String delim,        String source    ) {
        super(
        );
        this.to = to;
        this.value = value;
        this.delim = delim;
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


}