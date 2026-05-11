





import java.util.List;
import java.util.ArrayList;

public class fxg_GradientEntry extends FXGElement {

    private String alpha;
    private String ratio;
    private String color;



    public fxg_GradientEntry(
        String alpha,        String ratio,        String color    ) {
        super(
        );
        this.alpha = alpha;
        this.ratio = ratio;
        this.color = color;
    }


    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getRatio() {
        return ratio;
    }

    public void setRatio(String ratio) {
        this.ratio = ratio;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}