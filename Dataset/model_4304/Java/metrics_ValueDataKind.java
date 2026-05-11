





import java.util.List;
import java.util.ArrayList;

public class metrics_ValueDataKind extends DataKind {

    private String format;
    private String valueKind;
    private String kindHint;



    public metrics_ValueDataKind(
        String format,        String valueKind,        String kindHint    ) {
        super(
        );
        this.format = format;
        this.valueKind = valueKind;
        this.kindHint = kindHint;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
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


}