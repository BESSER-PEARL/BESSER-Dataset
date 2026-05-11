





import java.util.List;
import java.util.ArrayList;

public class graphgenerators_LatticeGraphGenerator extends GraphGenerator {

    private boolean periodicBoundaries;
    private boolean useNextNearestNeighbors;
    private boolean useNearestNeighbors;



    public graphgenerators_LatticeGraphGenerator(
        boolean periodicBoundaries,        boolean useNextNearestNeighbors,        boolean useNearestNeighbors    ) {
        super(
        );
        this.periodicBoundaries = periodicBoundaries;
        this.useNextNearestNeighbors = useNextNearestNeighbors;
        this.useNearestNeighbors = useNearestNeighbors;
    }


    public boolean getPeriodicboundaries() {
        return periodicBoundaries;
    }

    public void setPeriodicboundaries(boolean periodicBoundaries) {
        this.periodicBoundaries = periodicBoundaries;
    }
    public boolean getUsenextnearestneighbors() {
        return useNextNearestNeighbors;
    }

    public void setUsenextnearestneighbors(boolean useNextNearestNeighbors) {
        this.useNextNearestNeighbors = useNextNearestNeighbors;
    }
    public boolean getUsenearestneighbors() {
        return useNearestNeighbors;
    }

    public void setUsenearestneighbors(boolean useNearestNeighbors) {
        this.useNearestNeighbors = useNearestNeighbors;
    }


}