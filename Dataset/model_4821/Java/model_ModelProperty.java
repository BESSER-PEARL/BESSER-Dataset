





import java.util.List;
import java.util.ArrayList;

public class model_ModelProperty  {

    private String value;





    private model_ModelPropertyType model_modelpropertytype;


    public model_ModelProperty(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public model_ModelPropertyType getModel_modelpropertytype() {
        return model_modelpropertytype;
    }

    public void setModel_modelpropertytype(model_ModelPropertyType model_modelpropertytype) {
        this.model_modelpropertytype = model_modelpropertytype;
    }

}