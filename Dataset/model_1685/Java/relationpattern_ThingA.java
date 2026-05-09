




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class relationpattern_ThingA extends NamedElement, SourceNode {

    private LocalDate since;



    public relationpattern_ThingA(
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