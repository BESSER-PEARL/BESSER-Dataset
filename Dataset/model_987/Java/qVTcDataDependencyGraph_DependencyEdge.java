





import java.util.List;
import java.util.ArrayList;

public class qVTcDataDependencyGraph_DependencyEdge extends Edge {

    private String direction;
    private boolean derived;
    private boolean multiple;



    public qVTcDataDependencyGraph_DependencyEdge(
        String direction,        boolean derived,        boolean multiple    ) {
        super(
        );
        this.direction = direction;
        this.derived = derived;
        this.multiple = multiple;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }


}