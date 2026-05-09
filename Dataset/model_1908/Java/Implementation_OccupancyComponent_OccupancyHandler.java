





import java.util.List;
import java.util.ArrayList;

public class Implementation_OccupancyComponent_OccupancyHandler extends OccupancyComponent_IOccupancyDecision, OccupancyComponent_IOccupancy {






    private List<Implementation_OccupancyComponent_Occupancy> implementation_occupancycomponent_occupancys;


    public Implementation_OccupancyComponent_OccupancyHandler(
    ) {
        super(
        );
        this.implementation_occupancycomponent_occupancys = new ArrayList<>();
    }

    public Implementation_OccupancyComponent_OccupancyHandler(
        ArrayList<Implementation_OccupancyComponent_Occupancy> implementation_occupancycomponent_occupancys    ) {
        this.implementation_occupancycomponent_occupancys = implementation_occupancycomponent_occupancys;
    }


    public List<Implementation_OccupancyComponent_Occupancy> getImplementation_occupancycomponent_occupancys() {
        return implementation_occupancycomponent_occupancys;
    }

    public void addImplementation_occupancycomponent_occupancy(Implementation_occupancycomponent_occupancy implementation_occupancycomponent_occupancy) {
        this.implementation_occupancycomponent_occupancys.add(implementation_occupancycomponent_occupancy);
    }

}