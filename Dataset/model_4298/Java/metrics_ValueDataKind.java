





import java.util.List;
import java.util.ArrayList;

public class metrics_ValueDataKind extends DataKind {

    private String valueKind;



    public metrics_ValueDataKind(
        String valueKind    ) {
        super(
        );
        this.valueKind = valueKind;
    }


    public String getValuekind() {
        return valueKind;
    }

    public void setValuekind(String valueKind) {
        this.valueKind = valueKind;
    }


}