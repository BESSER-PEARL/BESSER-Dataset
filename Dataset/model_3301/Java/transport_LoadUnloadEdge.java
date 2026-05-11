





import java.util.List;
import java.util.ArrayList;

public class transport_LoadUnloadEdge extends MigrationEdge {

    private boolean loadingEdge;



    public transport_LoadUnloadEdge(
        boolean loadingEdge    ) {
        super(
        );
        this.loadingEdge = loadingEdge;
    }


    public boolean getLoadingedge() {
        return loadingEdge;
    }

    public void setLoadingedge(boolean loadingEdge) {
        this.loadingEdge = loadingEdge;
    }


}