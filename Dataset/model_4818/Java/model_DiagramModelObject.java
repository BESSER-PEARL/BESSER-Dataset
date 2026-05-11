





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelObject extends FontAttribute, TextAlignment, Connectable, LineObject {

    private String fillColor;
    private int alpha;





    private model_DiagramModelContainer model_diagrammodelcontainer;


    public model_DiagramModelObject(
        String fillColor,        int alpha    ) {
        super(
        );
        this.fillColor = fillColor;
        this.alpha = alpha;
    }


    public String getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(String fillColor) {
        this.fillColor = fillColor;
    }
    public int getAlpha() {
        return alpha;
    }

    public void setAlpha(int alpha) {
        this.alpha = alpha;
    }

    public model_DiagramModelContainer getModel_diagrammodelcontainer() {
        return model_diagrammodelcontainer;
    }

    public void setModel_diagrammodelcontainer(model_DiagramModelContainer model_diagrammodelcontainer) {
        this.model_diagrammodelcontainer = model_diagrammodelcontainer;
    }

}