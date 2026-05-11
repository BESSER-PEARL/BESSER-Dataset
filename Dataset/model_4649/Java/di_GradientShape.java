





import java.util.List;
import java.util.ArrayList;

public class di_GradientShape extends Shape {

    private boolean usingGradient;
    private boolean verticalGradient;
    private int gradientColor;



    public di_GradientShape(
        boolean usingGradient,        boolean verticalGradient,        int gradientColor    ) {
        super(
        );
        this.usingGradient = usingGradient;
        this.verticalGradient = verticalGradient;
        this.gradientColor = gradientColor;
    }


    public boolean getUsinggradient() {
        return usingGradient;
    }

    public void setUsinggradient(boolean usingGradient) {
        this.usingGradient = usingGradient;
    }
    public boolean getVerticalgradient() {
        return verticalGradient;
    }

    public void setVerticalgradient(boolean verticalGradient) {
        this.verticalGradient = verticalGradient;
    }
    public int getGradientcolor() {
        return gradientColor;
    }

    public void setGradientcolor(int gradientColor) {
        this.gradientColor = gradientColor;
    }


}