





import java.util.List;
import java.util.ArrayList;

public class sparrow_LoadCsv extends Action {

    private String source;
    private String delim;
    private String to;
    private String value;



    public sparrow_LoadCsv(
        String source,        String delim,        String to,        String value    ) {
        super(
        );
        this.source = source;
        this.delim = delim;
        this.to = to;
        this.value = value;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getDelim() {
        return delim;
    }

    public void setDelim(String delim) {
        this.delim = delim;
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