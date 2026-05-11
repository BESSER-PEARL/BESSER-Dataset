





import java.util.List;
import java.util.ArrayList;

public class dg_GradientStop  {

    private String color;
    private String offset;
    private String opacity;





    private dg_Gradient dg_gradient;


    public dg_GradientStop(
        String color,        String offset,        String opacity    ) {
        this.color = color;
        this.offset = offset;
        this.opacity = opacity;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getOpacity() {
        return opacity;
    }

    public void setOpacity(String opacity) {
        this.opacity = opacity;
    }

    public dg_Gradient getDg_gradient() {
        return dg_gradient;
    }

    public void setDg_gradient(dg_Gradient dg_gradient) {
        this.dg_gradient = dg_gradient;
    }

}