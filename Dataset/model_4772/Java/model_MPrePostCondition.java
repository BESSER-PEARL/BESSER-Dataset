





import java.util.List;
import java.util.ArrayList;

public class model_MPrePostCondition extends MModelElement {

    private int positionInModel;





    private model_MOperation model_moperation;




    private model_MModel model_mmodel;


    public model_MPrePostCondition(
        int positionInModel    ) {
        super(
        );
        this.positionInModel = positionInModel;
    }


    public int getPositioninmodel() {
        return positionInModel;
    }

    public void setPositioninmodel(int positionInModel) {
        this.positionInModel = positionInModel;
    }

    public model_MOperation getModel_moperation() {
        return model_moperation;
    }

    public void setModel_moperation(model_MOperation model_moperation) {
        this.model_moperation = model_moperation;
    }
    public model_MModel getModel_mmodel() {
        return model_mmodel;
    }

    public void setModel_mmodel(model_MModel model_mmodel) {
        this.model_mmodel = model_mmodel;
    }

}