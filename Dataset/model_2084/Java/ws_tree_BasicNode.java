





import java.util.List;
import java.util.ArrayList;

public class ws_tree_BasicNode extends Node {

    private String modelName;



    public ws_tree_BasicNode(
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