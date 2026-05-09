





import java.util.List;
import java.util.ArrayList;

public class qVTcDataDependencyGraph_ContainmentEdge extends Edge {

    private String model;



    public qVTcDataDependencyGraph_ContainmentEdge(
        String model    ) {
        super(
        );
        this.model = model;
    }


    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }


}