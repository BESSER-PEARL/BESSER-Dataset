





import java.util.List;
import java.util.ArrayList;

public class di_Diagram  {

    private String name;
    private String documentation;
    private float resolution;





    private di_DiagramElement di_diagramelement;




    private List<di_Style> di_styles;




    private di_DiagramElement di_diagramelement;


    public di_Diagram(
        String name,        String documentation,        float resolution    ) {
        this.name = name;
        this.documentation = documentation;
        this.resolution = resolution;
        this.di_styles = new ArrayList<>();
    }

    public di_Diagram(
        String name,        String documentation,        float resolution        ArrayList<di_Style> di_styles    ) {
        this.name = name;
        this.documentation = documentation;
        this.resolution = resolution;
        this.di_styles = di_styles;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public float getResolution() {
        return resolution;
    }

    public void setResolution(float resolution) {
        this.resolution = resolution;
    }

    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }
    public List<di_Style> getDi_styles() {
        return di_styles;
    }

    public void addDi_style(Di_style di_style) {
        this.di_styles.add(di_style);
    }
    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }

}