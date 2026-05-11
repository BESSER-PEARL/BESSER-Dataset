





import java.util.List;
import java.util.ArrayList;

public class Dimension  {






    private model_olap_OlapModel model_olap_olapmodel;




    private model_olap_Hierarchy model_olap_hierarchy;




    private model_olap_VirtualCubeDimension model_olap_virtualcubedimension;




    private model_olap_Cube model_olap_cube;


    public Dimension(
    ) {
    }



    public model_olap_OlapModel getModel_olap_olapmodel() {
        return model_olap_olapmodel;
    }

    public void setModel_olap_olapmodel(model_olap_OlapModel model_olap_olapmodel) {
        this.model_olap_olapmodel = model_olap_olapmodel;
    }
    public model_olap_Hierarchy getModel_olap_hierarchy() {
        return model_olap_hierarchy;
    }

    public void setModel_olap_hierarchy(model_olap_Hierarchy model_olap_hierarchy) {
        this.model_olap_hierarchy = model_olap_hierarchy;
    }
    public model_olap_VirtualCubeDimension getModel_olap_virtualcubedimension() {
        return model_olap_virtualcubedimension;
    }

    public void setModel_olap_virtualcubedimension(model_olap_VirtualCubeDimension model_olap_virtualcubedimension) {
        this.model_olap_virtualcubedimension = model_olap_virtualcubedimension;
    }
    public model_olap_Cube getModel_olap_cube() {
        return model_olap_cube;
    }

    public void setModel_olap_cube(model_olap_Cube model_olap_cube) {
        this.model_olap_cube = model_olap_cube;
    }

}