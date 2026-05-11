





import java.util.List;
import java.util.ArrayList;

public class model_Model extends ModelObject {






    private List<model_ModelPropertyType> model_modelpropertytypes;




    private List<model_ModelPropertyCategory> model_modelpropertycategorys;


    public model_Model(
    ) {
        super(
        );
        this.model_modelpropertytypes = new ArrayList<>();
        this.model_modelpropertycategorys = new ArrayList<>();
    }

    public model_Model(
        ArrayList<model_ModelPropertyType> model_modelpropertytypes,        ArrayList<model_ModelPropertyCategory> model_modelpropertycategorys    ) {
        this.model_modelpropertytypes = model_modelpropertytypes;
        this.model_modelpropertycategorys = model_modelpropertycategorys;
    }


    public List<model_ModelPropertyType> getModel_modelpropertytypes() {
        return model_modelpropertytypes;
    }

    public void addModel_modelpropertytype(Model_modelpropertytype model_modelpropertytype) {
        this.model_modelpropertytypes.add(model_modelpropertytype);
    }
    public List<model_ModelPropertyCategory> getModel_modelpropertycategorys() {
        return model_modelpropertycategorys;
    }

    public void addModel_modelpropertycategory(Model_modelpropertycategory model_modelpropertycategory) {
        this.model_modelpropertycategorys.add(model_modelpropertycategory);
    }

}