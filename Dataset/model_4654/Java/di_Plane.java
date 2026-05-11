





import java.util.List;
import java.util.ArrayList;

public class di_Plane extends Node {

    private String diagramElementGroup;



    public di_Plane(
        String diagramElementGroup    ) {
        super(
        );
        this.diagramElementGroup = diagramElementGroup;
    }


    public String getDiagramelementgroup() {
        return diagramElementGroup;
    }

    public void setDiagramelementgroup(String diagramElementGroup) {
        this.diagramElementGroup = diagramElementGroup;
    }


}