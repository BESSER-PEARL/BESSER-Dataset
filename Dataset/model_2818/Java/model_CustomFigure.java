





import java.util.List;
import java.util.ArrayList;

public class model_CustomFigure  {

    private String name;





    private model_ConnectableElement model_connectableelement;




    private model_XDiagram model_xdiagram;


    public model_CustomFigure(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_ConnectableElement getModel_connectableelement() {
        return model_connectableelement;
    }

    public void setModel_connectableelement(model_ConnectableElement model_connectableelement) {
        this.model_connectableelement = model_connectableelement;
    }
    public model_XDiagram getModel_xdiagram() {
        return model_xdiagram;
    }

    public void setModel_xdiagram(model_XDiagram model_xdiagram) {
        this.model_xdiagram = model_xdiagram;
    }

}