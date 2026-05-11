





import java.util.List;
import java.util.ArrayList;

public class draw2d_LabeledBorder extends Border {

    private String label;





    private draw2d_Font draw2d_font;


    public draw2d_LabeledBorder(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public draw2d_Font getDraw2d_font() {
        return draw2d_font;
    }

    public void setDraw2d_font(draw2d_Font draw2d_font) {
        this.draw2d_font = draw2d_font;
    }

}