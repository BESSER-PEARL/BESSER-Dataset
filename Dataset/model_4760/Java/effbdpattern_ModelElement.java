





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_ModelElement extends Indexable {

    private String modelName;
    private int modelId;



    public effbdpattern_ModelElement(
        String modelName,        int modelId    ) {
        super(
        );
        this.modelName = modelName;
        this.modelId = modelId;
    }


    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }
    public int getModelid() {
        return modelId;
    }

    public void setModelid(int modelId) {
        this.modelId = modelId;
    }


}