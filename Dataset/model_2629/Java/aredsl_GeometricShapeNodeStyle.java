





import java.util.List;
import java.util.ArrayList;

public class aredsl_GeometricShapeNodeStyle extends NodeStyle {

    private String color;
    private String outline;
    private String kind;



    public aredsl_GeometricShapeNodeStyle(
        String color,        String outline,        String kind    ) {
        super(
        );
        this.color = color;
        this.outline = outline;
        this.kind = kind;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getOutline() {
        return outline;
    }

    public void setOutline(String outline) {
        this.outline = outline;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}