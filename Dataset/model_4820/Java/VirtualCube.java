





import java.util.List;
import java.util.ArrayList;

public class VirtualCube  {






    private model_olap_OlapModel model_olap_olapmodel;




    private model_olap_VirtualCubeDimension model_olap_virtualcubedimension;




    private model_olap_VirtualCubeMeasure model_olap_virtualcubemeasure;


    public VirtualCube(
    ) {
    }



    public model_olap_OlapModel getModel_olap_olapmodel() {
        return model_olap_olapmodel;
    }

    public void setModel_olap_olapmodel(model_olap_OlapModel model_olap_olapmodel) {
        this.model_olap_olapmodel = model_olap_olapmodel;
    }
    public model_olap_VirtualCubeDimension getModel_olap_virtualcubedimension() {
        return model_olap_virtualcubedimension;
    }

    public void setModel_olap_virtualcubedimension(model_olap_VirtualCubeDimension model_olap_virtualcubedimension) {
        this.model_olap_virtualcubedimension = model_olap_virtualcubedimension;
    }
    public model_olap_VirtualCubeMeasure getModel_olap_virtualcubemeasure() {
        return model_olap_virtualcubemeasure;
    }

    public void setModel_olap_virtualcubemeasure(model_olap_VirtualCubeMeasure model_olap_virtualcubemeasure) {
        this.model_olap_virtualcubemeasure = model_olap_virtualcubemeasure;
    }

}