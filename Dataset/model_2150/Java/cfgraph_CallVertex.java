





import java.util.List;
import java.util.ArrayList;

public class cfgraph_CallVertex extends StatementVertex {






    private cfgraph_StartVertex cfgraph_startvertex;


    public cfgraph_CallVertex(
    ) {
        super(
        );
    }



    public cfgraph_StartVertex getCfgraph_startvertex() {
        return cfgraph_startvertex;
    }

    public void setCfgraph_startvertex(cfgraph_StartVertex cfgraph_startvertex) {
        this.cfgraph_startvertex = cfgraph_startvertex;
    }

}