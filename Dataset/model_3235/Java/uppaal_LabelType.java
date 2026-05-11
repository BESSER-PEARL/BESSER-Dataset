





import java.util.List;
import java.util.ArrayList;

public class uppaal_LabelType  {

    private String mixed;
    private String x;
    private String kind;
    private String y;



    public uppaal_LabelType(
        String mixed,        String x,        String kind,        String y    ) {
        this.mixed = mixed;
        this.x = x;
        this.kind = kind;
        this.y = y;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }


}