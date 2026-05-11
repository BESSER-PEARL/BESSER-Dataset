





import java.util.List;
import java.util.ArrayList;

public class model_Dimension  {

    private float height;
    private float width;





    private model_Symbol model_symbol;




    private model_Figure model_figure;


    public model_Dimension(
        float height,        float width    ) {
        this.height = height;
        this.width = width;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public model_Symbol getModel_symbol() {
        return model_symbol;
    }

    public void setModel_symbol(model_Symbol model_symbol) {
        this.model_symbol = model_symbol;
    }
    public model_Figure getModel_figure() {
        return model_figure;
    }

    public void setModel_figure(model_Figure model_figure) {
        this.model_figure = model_figure;
    }

}