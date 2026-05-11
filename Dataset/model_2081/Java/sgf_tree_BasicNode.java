





import java.util.List;
import java.util.ArrayList;

public class sgf_tree_BasicNode extends Node {

    private String modelName;



    public sgf_tree_BasicNode(
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