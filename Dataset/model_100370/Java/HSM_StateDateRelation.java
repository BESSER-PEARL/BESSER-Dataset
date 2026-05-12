





import java.util.List;
import java.util.ArrayList;

public class HSM_StateDateRelation extends MgaObject {

    private String color;
    private String value;



    public HSM_StateDateRelation(
        String color,        String value    ) {
        super(
        );
        this.color = color;
        this.value = value;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}