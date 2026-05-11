





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Dimension  {

    private float width;
    private float height;





    private VisualInterface_Symbol visualinterface_symbol;


    public VisualInterface_Dimension(
        float width,        float height    ) {
        this.width = width;
        this.height = height;
    }


    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    public VisualInterface_Symbol getVisualinterface_symbol() {
        return visualinterface_symbol;
    }

    public void setVisualinterface_symbol(VisualInterface_Symbol visualinterface_symbol) {
        this.visualinterface_symbol = visualinterface_symbol;
    }

}