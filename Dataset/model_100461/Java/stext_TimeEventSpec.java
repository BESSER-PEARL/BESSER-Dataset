





import java.util.List;
import java.util.ArrayList;

public class stext_TimeEventSpec extends EventSpec {

    private String type;
    private String unit;



    public stext_TimeEventSpec(
        String type,        String unit    ) {
        super(
        );
        this.type = type;
        this.unit = unit;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}