





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelZentaObject extends DiagramModelObject, DiagramModelContainer {

    private int type;





    private model_ZentaElement model_zentaelement;




    private model_ZentaElement model_zentaelement;


    public model_DiagramModelZentaObject(
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

    public model_ZentaElement getModel_zentaelement() {
        return model_zentaelement;
    }

    public void setModel_zentaelement(model_ZentaElement model_zentaelement) {
        this.model_zentaelement = model_zentaelement;
    }
    public model_ZentaElement getModel_zentaelement() {
        return model_zentaelement;
    }

    public void setModel_zentaelement(model_ZentaElement model_zentaelement) {
        this.model_zentaelement = model_zentaelement;
    }

}