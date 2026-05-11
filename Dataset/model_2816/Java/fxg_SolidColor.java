





import java.util.List;
import java.util.ArrayList;

public class fxg_SolidColor extends Fill {

    private String alpha;
    private String color;



    public fxg_SolidColor(
        String alpha,        String color    ) {
        super(
        );
        this.alpha = alpha;
        this.color = color;
    }


    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}