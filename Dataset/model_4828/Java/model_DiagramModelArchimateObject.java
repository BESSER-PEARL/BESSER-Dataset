





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelArchimateObject extends DiagramModelArchimateComponent, DiagramModelObject, TextPosition, DiagramModelContainer {

    private int type;





    private model_ArchimateElement model_archimateelement;


    public model_DiagramModelArchimateObject(
        int type    ) {
        super(
        );
        this.type = type;
    }


    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public model_ArchimateElement getModel_archimateelement() {
        return model_archimateelement;
    }

    public void setModel_archimateelement(model_ArchimateElement model_archimateelement) {
        this.model_archimateelement = model_archimateelement;
    }

}