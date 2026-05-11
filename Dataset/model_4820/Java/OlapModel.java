





import java.util.List;
import java.util.ArrayList;

public class OlapModel  {






    private model_Model model_model;




    private model_olap_VirtualCube model_olap_virtualcube;




    private model_olap_Cube model_olap_cube;




    private model_olap_Dimension model_olap_dimension;


    public OlapModel(
    ) {
    }



    public model_Model getModel_model() {
        return model_model;
    }

    public void setModel_model(model_Model model_model) {
        this.model_model = model_model;
    }
    public model_olap_VirtualCube getModel_olap_virtualcube() {
        return model_olap_virtualcube;
    }

    public void setModel_olap_virtualcube(model_olap_VirtualCube model_olap_virtualcube) {
        this.model_olap_virtualcube = model_olap_virtualcube;
    }
    public model_olap_Cube getModel_olap_cube() {
        return model_olap_cube;
    }

    public void setModel_olap_cube(model_olap_Cube model_olap_cube) {
        this.model_olap_cube = model_olap_cube;
    }
    public model_olap_Dimension getModel_olap_dimension() {
        return model_olap_dimension;
    }

    public void setModel_olap_dimension(model_olap_Dimension model_olap_dimension) {
        this.model_olap_dimension = model_olap_dimension;
    }

}