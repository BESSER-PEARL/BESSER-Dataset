





import java.util.List;
import java.util.ArrayList;

public class metrics_ValueDataKind extends DataKind {

    private String valueKind;
    private String kindHint;
    private String format;



    public metrics_ValueDataKind(
        String valueKind,        String kindHint,        String format    ) {
        super(
        );
        this.valueKind = valueKind;
        this.kindHint = kindHint;
        this.format = format;
    }


    public String getValuekind() {
        return valueKind;
    }

    public void setValuekind(String valueKind) {
        this.valueKind = valueKind;
    }
    public String getKindhint() {
        return kindHint;
    }

    public void setKindhint(String kindHint) {
        this.kindHint = kindHint;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}