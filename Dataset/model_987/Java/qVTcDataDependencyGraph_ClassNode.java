





import java.util.List;
import java.util.ArrayList;

public class qVTcDataDependencyGraph_ClassNode extends Node {

    private String model;
    private String superTypes;



    public qVTcDataDependencyGraph_ClassNode(
        String model,        String superTypes    ) {
        super(
        );
        this.model = model;
        this.superTypes = superTypes;
    }


    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public String getSupertypes() {
        return superTypes;
    }

    public void setSupertypes(String superTypes) {
        this.superTypes = superTypes;
    }


}