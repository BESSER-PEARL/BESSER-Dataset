





import java.util.List;
import java.util.ArrayList;

public class fxg_BitmapFill extends Fill {

    private String scaleY;
    private String scaleX;
    private String rotation;
    private String fillMode;
    private String source;
    private String x;
    private String y;





    private fxg_Matrix fxg_matrix;


    public fxg_BitmapFill(
        String scaleY,        String scaleX,        String rotation,        String fillMode,        String source,        String x,        String y    ) {
        super(
        );
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.rotation = rotation;
        this.fillMode = fillMode;
        this.source = source;
        this.x = x;
        this.y = y;
    }


    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getFillmode() {
        return fillMode;
    }

    public void setFillmode(String fillMode) {
        this.fillMode = fillMode;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}