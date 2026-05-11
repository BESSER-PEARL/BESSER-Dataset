





import java.util.List;
import java.util.ArrayList;

public class fxg_SolidColor extends Fill {

    private String color;
    private String alpha;



    public fxg_SolidColor(
        String color,        String alpha    ) {
        super(
        );
        this.color = color;
        this.alpha = alpha;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }


}