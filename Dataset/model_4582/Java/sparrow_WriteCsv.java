





import java.util.List;
import java.util.ArrayList;

public class sparrow_WriteCsv extends Action {

    private String to;
    private String delim;
    private String value;
    private String source;



    public sparrow_WriteCsv(
        String to,        String delim,        String value,        String source    ) {
        super(
        );
        this.to = to;
        this.delim = delim;
        this.value = value;
        this.source = source;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getDelim() {
        return delim;
    }

    public void setDelim(String delim) {
        this.delim = delim;
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