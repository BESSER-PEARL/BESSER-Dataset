





import java.util.List;
import java.util.ArrayList;

public class model_Domain extends FQNamedElement, Type {

    private String type;





    private model_Schema model_schema;


    public model_Domain(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_Schema getModel_schema() {
        return model_schema;
    }

    public void setModel_schema(model_Schema model_schema) {
        this.model_schema = model_schema;
    }

}