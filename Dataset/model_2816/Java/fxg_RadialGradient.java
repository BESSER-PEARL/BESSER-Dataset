





import java.util.List;
import java.util.ArrayList;

public class fxg_RadialGradient  {

    private String scaleX;
    private String scaleY;
    private String spreadMethod;
    private String x;
    private String rotation;
    private String y;
    private String interpolationMethod;
    private String focalPointRatio;





    private fxg_Matrix fxg_matrix;


    public fxg_RadialGradient(
        String scaleX,        String scaleY,        String spreadMethod,        String x,        String rotation,        String y,        String interpolationMethod,        String focalPointRatio    ) {
        this.scaleX = scaleX;
        this.scaleY = scaleY;
        this.spreadMethod = spreadMethod;
        this.x = x;
        this.rotation = rotation;
        this.y = y;
        this.interpolationMethod = interpolationMethod;
        this.focalPointRatio = focalPointRatio;
    }


    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getSpreadmethod() {
        return spreadMethod;
    }

    public void setSpreadmethod(String spreadMethod) {
        this.spreadMethod = spreadMethod;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getInterpolationmethod() {
        return interpolationMethod;
    }

    public void setInterpolationmethod(String interpolationMethod) {
        this.interpolationMethod = interpolationMethod;
    }
    public String getFocalpointratio() {
        return focalPointRatio;
    }

    public void setFocalpointratio(String focalPointRatio) {
        this.focalPointRatio = focalPointRatio;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}