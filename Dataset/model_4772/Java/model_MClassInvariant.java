





import java.util.List;
import java.util.ArrayList;

public class model_MClassInvariant extends MModelElement {

    private String name;
    private int positionInModel;





    private model_MClass model_mclass;




    private model_MModel model_mmodel;


    public model_MClassInvariant(
        String name,        int positionInModel    ) {
        super(
        );
        this.name = name;
        this.positionInModel = positionInModel;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPositioninmodel() {
        return positionInModel;
    }

    public void setPositioninmodel(int positionInModel) {
        this.positionInModel = positionInModel;
    }

    public model_MClass getModel_mclass() {
        return model_mclass;
    }

    public void setModel_mclass(model_MClass model_mclass) {
        this.model_mclass = model_mclass;
    }
    public model_MModel getModel_mmodel() {
        return model_mmodel;
    }

    public void setModel_mmodel(model_MModel model_mmodel) {
        this.model_mmodel = model_mmodel;
    }

}