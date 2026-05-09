





import java.util.List;
import java.util.ArrayList;

public class mMDSL_ModelCreate  {

    private String name;





    private mMDSL_ModelType mmdsl_modeltype;




    private mMDSL_ModelOperation mmdsl_modeloperation;


    public mMDSL_ModelCreate(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_ModelType getMmdsl_modeltype() {
        return mmdsl_modeltype;
    }

    public void setMmdsl_modeltype(mMDSL_ModelType mmdsl_modeltype) {
        this.mmdsl_modeltype = mmdsl_modeltype;
    }
    public mMDSL_ModelOperation getMmdsl_modeloperation() {
        return mmdsl_modeloperation;
    }

    public void setMmdsl_modeloperation(mMDSL_ModelOperation mmdsl_modeloperation) {
        this.mmdsl_modeloperation = mmdsl_modeloperation;
    }

}