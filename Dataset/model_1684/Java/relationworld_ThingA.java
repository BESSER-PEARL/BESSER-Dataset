




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class relationworld_ThingA extends NamedElement, SourceNode {

    private LocalDate since;





    private relationworld_World relationworld_world;


    public relationworld_ThingA(
        LocalDate since    ) {
        super(
        );
        this.since = since;
    }


    public LocalDate getSince() {
        return since;
    }

    public void setSince(LocalDate since) {
        this.since = since;
    }

    public relationworld_World getRelationworld_world() {
        return relationworld_world;
    }

    public void setRelationworld_world(relationworld_World relationworld_world) {
        this.relationworld_world = relationworld_world;
    }

}