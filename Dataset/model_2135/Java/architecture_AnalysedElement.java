





import java.util.List;
import java.util.ArrayList;

public class architecture_AnalysedElement  {

    private int idAnalyzedElement;
    private int properties;
    private String name;





    private List<architecture_AnalysedElement> architecture_analysedelements;




    private architecture_AnalysedElement architecture_analysedelement;


    public architecture_AnalysedElement(
        int idAnalyzedElement,        int properties,        String name    ) {
        this.idAnalyzedElement = idAnalyzedElement;
        this.properties = properties;
        this.name = name;
        this.architecture_analysedelements = new ArrayList<>();
    }

    public architecture_AnalysedElement(
        int idAnalyzedElement,        int properties,        String name        ArrayList<architecture_AnalysedElement> architecture_analysedelements    ) {
        this.idAnalyzedElement = idAnalyzedElement;
        this.properties = properties;
        this.name = name;
        this.architecture_analysedelements = architecture_analysedelements;
    }

    public int getIdanalyzedelement() {
        return idAnalyzedElement;
    }

    public void setIdanalyzedelement(int idAnalyzedElement) {
        this.idAnalyzedElement = idAnalyzedElement;
    }
    public int getProperties() {
        return properties;
    }

    public void setProperties(int properties) {
        this.properties = properties;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<architecture_AnalysedElement> getArchitecture_analysedelements() {
        return architecture_analysedelements;
    }

    public void addArchitecture_analysedelement(Architecture_analysedelement architecture_analysedelement) {
        this.architecture_analysedelements.add(architecture_analysedelement);
    }
    public architecture_AnalysedElement getArchitecture_analysedelement() {
        return architecture_analysedelement;
    }

    public void setArchitecture_analysedelement(architecture_AnalysedElement architecture_analysedelement) {
        this.architecture_analysedelement = architecture_analysedelement;
    }

}