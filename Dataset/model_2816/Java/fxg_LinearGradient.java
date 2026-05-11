





import java.util.List;
import java.util.ArrayList;

public class fxg_LinearGradient  {

    private String interpolationMethod;
    private String rotation;
    private String scaleX;
    private String y;
    private String x;
    private String spreadMethod;





    private fxg_Matrix fxg_matrix;


    public fxg_LinearGradient(
        String interpolationMethod,        String rotation,        String scaleX,        String y,        String x,        String spreadMethod    ) {
        this.interpolationMethod = interpolationMethod;
        this.rotation = rotation;
        this.scaleX = scaleX;
        this.y = y;
        this.x = x;
        this.spreadMethod = spreadMethod;
    }


    public String getInterpolationmethod() {
        return interpolationMethod;
    }

    public void setInterpolationmethod(String interpolationMethod) {
        this.interpolationMethod = interpolationMethod;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getSpreadmethod() {
        return spreadMethod;
    }

    public void setSpreadmethod(String spreadMethod) {
        this.spreadMethod = spreadMethod;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}