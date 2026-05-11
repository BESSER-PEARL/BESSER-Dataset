





import java.util.List;
import java.util.ArrayList;

public class di_Diagram  {

    private float resolution;
    private String documentation;
    private String name;





    private di_DiagramElement di_diagramelement;




    private di_DiagramElement di_diagramelement;


    public di_Diagram(
        float resolution,        String documentation,        String name    ) {
        this.resolution = resolution;
        this.documentation = documentation;
        this.name = name;
    }


    public float getResolution() {
        return resolution;
    }

    public void setResolution(float resolution) {
        this.resolution = resolution;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }
    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }

}