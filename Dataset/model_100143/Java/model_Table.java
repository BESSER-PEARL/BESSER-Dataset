





import java.util.List;
import java.util.ArrayList;

public class model_Table extends NamedElement, DescribedElement, FQNamedElement {






    private model_Schema model_schema;


    public model_Table(
    ) {
        super(
        );
    }



    public model_Schema getModel_schema() {
        return model_schema;
    }

    public void setModel_schema(model_Schema model_schema) {
        this.model_schema = model_schema;
    }

}