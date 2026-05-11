





import java.util.List;
import java.util.ArrayList;

public class dfg_DfgVertex  {

    private String mappings;





    private List<dfg_DfgVertex> dfg_dfgvertexs;




    private dfg_DfgGraph dfg_dfggraph;


    public dfg_DfgVertex(
        String mappings    ) {
        this.mappings = mappings;
        this.dfg_dfgvertexs = new ArrayList<>();
    }

    public dfg_DfgVertex(
        String mappings        ArrayList<dfg_DfgVertex> dfg_dfgvertexs    ) {
        this.mappings = mappings;
        this.dfg_dfgvertexs = dfg_dfgvertexs;
    }

    public String getMappings() {
        return mappings;
    }

    public void setMappings(String mappings) {
        this.mappings = mappings;
    }

    public List<dfg_DfgVertex> getDfg_dfgvertexs() {
        return dfg_dfgvertexs;
    }

    public void addDfg_dfgvertex(Dfg_dfgvertex dfg_dfgvertex) {
        this.dfg_dfgvertexs.add(dfg_dfgvertex);
    }
    public dfg_DfgGraph getDfg_dfggraph() {
        return dfg_dfggraph;
    }

    public void setDfg_dfggraph(dfg_DfgGraph dfg_dfggraph) {
        this.dfg_dfggraph = dfg_dfggraph;
    }

}