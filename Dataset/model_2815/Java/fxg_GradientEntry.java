





import java.util.List;
import java.util.ArrayList;

public class fxg_GradientEntry extends FXGElement {

    private String color;
    private String ratio;
    private String alpha;



    public fxg_GradientEntry(
        String color,        String ratio,        String alpha    ) {
        super(
        );
        this.color = color;
        this.ratio = ratio;
        this.alpha = alpha;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getRatio() {
        return ratio;
    }

    public void setRatio(String ratio) {
        this.ratio = ratio;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }


}