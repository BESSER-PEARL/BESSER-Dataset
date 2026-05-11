





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelArchimateObject extends DiagramModelContainer, DiagramModelObject, TextPosition, DiagramModelArchimateComponent {

    private String figureDelegateType;





    private model_ArchimateElement model_archimateelement;


    public model_DiagramModelArchimateObject(
        String figureDelegateType    ) {
        super(
        );
        this.figureDelegateType = figureDelegateType;
    }


    public String getFiguredelegatetype() {
        return figureDelegateType;
    }

    public void setFiguredelegatetype(String figureDelegateType) {
        this.figureDelegateType = figureDelegateType;
    }

    public model_ArchimateElement getModel_archimateelement() {
        return model_archimateelement;
    }

    public void setModel_archimateelement(model_ArchimateElement model_archimateelement) {
        this.model_archimateelement = model_archimateelement;
    }

}