





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModel extends DiagramModelContainer, Documentable, Properties, ArchimateModelObject {

    private int connectionRouterType;



    public model_DiagramModel(
        int connectionRouterType    ) {
        super(
        );
        this.connectionRouterType = connectionRouterType;
    }


    public int getConnectionroutertype() {
        return connectionRouterType;
    }

    public void setConnectionroutertype(int connectionRouterType) {
        this.connectionRouterType = connectionRouterType;
    }


}