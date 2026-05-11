





import java.util.List;
import java.util.ArrayList;

public class simulink_ModelReference extends Reference {

    private String modelName;



    public simulink_ModelReference(
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