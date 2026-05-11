





import java.util.List;
import java.util.ArrayList;

public class fxg_RadialGradient  {

    private String scaleX;
    private String focalPointRatio;
    private String spreadMethod;
    private String interpolationMethod;
    private String y;
    private String rotation;
    private String x;
    private String scaleY;





    private fxg_Matrix fxg_matrix;


    public fxg_RadialGradient(
        String scaleX,        String focalPointRatio,        String spreadMethod,        String interpolationMethod,        String y,        String rotation,        String x,        String scaleY    ) {
        this.scaleX = scaleX;
        this.focalPointRatio = focalPointRatio;
        this.spreadMethod = spreadMethod;
        this.interpolationMethod = interpolationMethod;
        this.y = y;
        this.rotation = rotation;
        this.x = x;
        this.scaleY = scaleY;
    }


    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getFocalpointratio() {
        return focalPointRatio;
    }

    public void setFocalpointratio(String focalPointRatio) {
        this.focalPointRatio = focalPointRatio;
    }
    public String getSpreadmethod() {
        return spreadMethod;
    }

    public void setSpreadmethod(String spreadMethod) {
        this.spreadMethod = spreadMethod;
    }
    public String getInterpolationmethod() {
        return interpolationMethod;
    }

    public void setInterpolationmethod(String interpolationMethod) {
        this.interpolationMethod = interpolationMethod;
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