





import java.util.List;
import java.util.ArrayList;

public class model_datasources_SerializableQueryResult extends AQueryResult {

    private String values;



    public model_datasources_SerializableQueryResult(
        String values    ) {
        super(
        );
        this.values = values;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }


}