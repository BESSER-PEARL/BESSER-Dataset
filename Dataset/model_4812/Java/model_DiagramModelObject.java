





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelObject extends FontAttribute, DiagramModelComponent {

    private String elementShape;
    private String fillColor;





    private model_DiagramModelContainer model_diagrammodelcontainer;


    public model_DiagramModelObject(
        String elementShape,        String fillColor    ) {
        super(
        );
        this.elementShape = elementShape;
        this.fillColor = fillColor;
    }


    public String getElementshape() {
        return elementShape;
    }

    public void setElementshape(String elementShape) {
        this.elementShape = elementShape;
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

}