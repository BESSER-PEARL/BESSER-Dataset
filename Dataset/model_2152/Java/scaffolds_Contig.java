





import java.util.List;
import java.util.ArrayList;

public class scaffolds_Contig  {

    private int length;
    private int multiplicity;





    private scaffolds_ScaffoldGraph scaffolds_scaffoldgraph;


    public scaffolds_Contig(
        int length,        int multiplicity    ) {
        this.length = length;
        this.multiplicity = multiplicity;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(int multiplicity) {
        this.multiplicity = multiplicity;
    }

    public scaffolds_ScaffoldGraph getScaffolds_scaffoldgraph() {
        return scaffolds_scaffoldgraph;
    }

    public void setScaffolds_scaffoldgraph(scaffolds_ScaffoldGraph scaffolds_scaffoldgraph) {
        this.scaffolds_scaffoldgraph = scaffolds_scaffoldgraph;
    }

}