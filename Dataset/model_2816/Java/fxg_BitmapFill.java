





import java.util.List;
import java.util.ArrayList;

public class fxg_BitmapFill extends Fill {

    private String source;
    private String scaleX;
    private String y;
    private String rotation;
    private String x;
    private String fillMode;
    private String scaleY;





    private fxg_Matrix fxg_matrix;


    public fxg_BitmapFill(
        String source,        String scaleX,        String y,        String rotation,        String x,        String fillMode,        String scaleY    ) {
        super(
        );
        this.source = source;
        this.scaleX = scaleX;
        this.y = y;
        this.rotation = rotation;
        this.x = x;
        this.fillMode = fillMode;
        this.scaleY = scaleY;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getFillmode() {
        return fillMode;
    }

    public void setFillmode(String fillMode) {
        this.fillMode = fillMode;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}