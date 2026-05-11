





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelObject extends TextAlignment, Connectable, LineObject, FontAttribute {

    private String fillColor;





    private model_DiagramModelContainer model_diagrammodelcontainer;




    private model_Bounds model_bounds;


    public model_DiagramModelObject(
        String fillColor    ) {
        super(
        );
        this.fillColor = fillColor;
    }


    public String getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(String fillColor) {
        this.fillColor = fillColor;
    }

    public model_DiagramModelContainer getModel_diagrammodelcontainer() {
        return model_diagrammodelcontainer;
    }

    public void setModel_diagrammodelcontainer(model_DiagramModelContainer model_diagrammodelcontainer) {
        this.model_diagrammodelcontainer = model_diagrammodelcontainer;
    }
    public model_Bounds getModel_bounds() {
        return model_bounds;
    }

    public void setModel_bounds(model_Bounds model_bounds) {
        this.model_bounds = model_bounds;
    }

}