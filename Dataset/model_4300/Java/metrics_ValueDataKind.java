





import java.util.List;
import java.util.ArrayList;

public class metrics_ValueDataKind extends DataKind {

    private String valueKind;
    private String format;
    private String kindHint;



    public metrics_ValueDataKind(
        String valueKind,        String format,        String kindHint    ) {
        super(
        );
        this.valueKind = valueKind;
        this.format = format;
        this.kindHint = kindHint;
    }


    public String getValuekind() {
        return valueKind;
    }

    public void setValuekind(String valueKind) {
        this.valueKind = valueKind;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getKindhint() {
        return kindHint;
    }

    public void setKindhint(String kindHint) {
        this.kindHint = kindHint;
    }


}