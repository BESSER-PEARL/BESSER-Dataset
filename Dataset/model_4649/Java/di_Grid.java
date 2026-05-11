





import java.util.List;
import java.util.ArrayList;

public class di_Grid  {

    private int color;
    private String style;
    private int spacing;





    private di_Diagram di_diagram;


    public di_Grid(
        int color,        String style,        int spacing    ) {
        this.color = color;
        this.style = style;
        this.spacing = spacing;
    }


    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public int getSpacing() {
        return spacing;
    }

    public void setSpacing(int spacing) {
        this.spacing = spacing;
    }

    public di_Diagram getDi_diagram() {
        return di_diagram;
    }

    public void setDi_diagram(di_Diagram di_diagram) {
        this.di_diagram = di_diagram;
    }

}