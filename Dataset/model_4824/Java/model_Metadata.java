





import java.util.List;
import java.util.ArrayList;

public class model_Metadata  {






    private List<model_Property> model_propertys;




    private model_ArchimateModel model_archimatemodel;


    public model_Metadata(
    ) {
        this.model_propertys = new ArrayList<>();
    }

    public model_Metadata(
        ArrayList<model_Property> model_propertys    ) {
        this.model_propertys = model_propertys;
    }


    public List<model_Property> getModel_propertys() {
        return model_propertys;
    }

    public void addModel_property(Model_property model_property) {
        this.model_propertys.add(model_property);
    }
    public model_ArchimateModel getModel_archimatemodel() {
        return model_archimatemodel;
    }

    public void setModel_archimatemodel(model_ArchimateModel model_archimatemodel) {
        this.model_archimatemodel = model_archimatemodel;
    }

}