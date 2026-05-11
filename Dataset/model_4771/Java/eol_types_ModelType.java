





import java.util.List;
import java.util.ArrayList;

public class eol_types_ModelType extends AnyType {

    private String modelName;



    public eol_types_ModelType(
        String modelName    ) {
        super(
        );
        this.modelName = modelName;
    }


    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }


}