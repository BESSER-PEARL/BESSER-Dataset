





import java.util.List;
import java.util.ArrayList;

public class di_Plane extends Node {






    private List<di_DiagramElement> di_diagramelements;


    public di_Plane(
    ) {
        super(
        );
        this.di_diagramelements = new ArrayList<>();
    }

    public di_Plane(
        ArrayList<di_DiagramElement> di_diagramelements    ) {
        this.di_diagramelements = di_diagramelements;
    }


    public List<di_DiagramElement> getDi_diagramelements() {
        return di_diagramelements;
    }

    public void addDi_diagramelement(Di_diagramelement di_diagramelement) {
        this.di_diagramelements.add(di_diagramelement);
    }

}