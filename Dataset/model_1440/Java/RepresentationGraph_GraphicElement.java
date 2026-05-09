





import java.util.List;
import java.util.ArrayList;

public class RepresentationGraph_GraphicElement  {

    private String paletteIconPath;
    private String paletteName;
    private String color;





    private RepresentationGraph_Diagram representationgraph_diagram;


    public RepresentationGraph_GraphicElement(
        String paletteIconPath,        String paletteName,        String color    ) {
        this.paletteIconPath = paletteIconPath;
        this.paletteName = paletteName;
        this.color = color;
    }


    public String getPaletteiconpath() {
        return paletteIconPath;
    }

    public void setPaletteiconpath(String paletteIconPath) {
        this.paletteIconPath = paletteIconPath;
    }
    public String getPalettename() {
        return paletteName;
    }

    public void setPalettename(String paletteName) {
        this.paletteName = paletteName;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public RepresentationGraph_Diagram getRepresentationgraph_diagram() {
        return representationgraph_diagram;
    }

    public void setRepresentationgraph_diagram(RepresentationGraph_Diagram representationgraph_diagram) {
        this.representationgraph_diagram = representationgraph_diagram;
    }

}