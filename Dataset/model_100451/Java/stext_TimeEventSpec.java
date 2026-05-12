





import java.util.List;
import java.util.ArrayList;

public class stext_TimeEventSpec extends EventSpec {

    private String unit;
    private String type;



    public stext_TimeEventSpec(
        String unit,        String type    ) {
        super(
        );
        this.unit = unit;
        this.type = type;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}