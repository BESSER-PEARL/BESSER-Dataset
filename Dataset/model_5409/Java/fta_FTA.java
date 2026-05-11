





import java.util.List;
import java.util.ArrayList;

public class fta_FTA  {






    private List<fta_Diagram> fta_diagrams;


    public fta_FTA(
    ) {
        this.fta_diagrams = new ArrayList<>();
    }

    public fta_FTA(
        ArrayList<fta_Diagram> fta_diagrams    ) {
        this.fta_diagrams = fta_diagrams;
    }


    public List<fta_Diagram> getFta_diagrams() {
        return fta_diagrams;
    }

    public void addFta_diagram(Fta_diagram fta_diagram) {
        this.fta_diagrams.add(fta_diagram);
    }

}