




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class relationworld_ThingA extends SourceNode, NamedElement {

    private LocalDate since;



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


}