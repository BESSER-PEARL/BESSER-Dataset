





import java.util.List;
import java.util.ArrayList;

public class architecture_AnalysedElement  {

    private int idAnalyzedElement;
    private String name;
    private int properties;





    private List<architecture_AnalysedElement> architecture_analysedelements;




    private architecture_AnalysedElement architecture_analysedelement;


    public architecture_AnalysedElement(
        int idAnalyzedElement,        String name,        int properties    ) {
        this.idAnalyzedElement = idAnalyzedElement;
        this.name = name;
        this.properties = properties;
        this.architecture_analysedelements = new ArrayList<>();
    }

    public architecture_AnalysedElement(
        int idAnalyzedElement,        String name,        int properties        ArrayList<architecture_AnalysedElement> architecture_analysedelements    ) {
        this.idAnalyzedElement = idAnalyzedElement;
        this.name = name;
        this.properties = properties;
        this.architecture_analysedelements = architecture_analysedelements;
    }

    public int getIdanalyzedelement() {
        return idAnalyzedElement;
    }

    public void setIdanalyzedelement(int idAnalyzedElement) {
        this.idAnalyzedElement = idAnalyzedElement;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getProperties() {
        return properties;
    }

    public void setProperties(int properties) {
        this.properties = properties;
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