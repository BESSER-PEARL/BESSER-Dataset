





import java.util.List;
import java.util.ArrayList;

public class model_MappingFile extends Mapping {






    private List<model_Field> model_fields;




    private model_Field model_field;


    public model_MappingFile(
    ) {
        super(
        );
        this.model_fields = new ArrayList<>();
    }

    public model_MappingFile(
        ArrayList<model_Field> model_fields    ) {
        this.model_fields = model_fields;
    }


    public List<model_Field> getModel_fields() {
        return model_fields;
    }

    public void addModel_field(Model_field model_field) {
        this.model_fields.add(model_field);
    }
    public model_Field getModel_field() {
        return model_field;
    }

    public void setModel_field(model_Field model_field) {
        this.model_field = model_field;
    }

}