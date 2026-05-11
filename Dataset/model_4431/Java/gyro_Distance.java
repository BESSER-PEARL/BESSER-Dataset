





import java.util.List;
import java.util.ArrayList;

public class gyro_Distance extends Condition {

    private int value;
    private String kind;



    public gyro_Distance(
        int value,        String kind    ) {
        super(
        );
        this.value = value;
        this.kind = kind;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}