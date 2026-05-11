





import java.util.List;
import java.util.ArrayList;

public class archimateC3_ArchimateElement  {

    private String description;
    private String elementName;





    private List<archimateC3_ArchimateElement> archimatec3_archimateelements;




    private archimateC3_ArchimateElement archimatec3_archimateelement;




    private archimateC3_ArchimateModel archimatec3_archimatemodel;


    public archimateC3_ArchimateElement(
        String description,        String elementName    ) {
        this.description = description;
        this.elementName = elementName;
        this.archimatec3_archimateelements = new ArrayList<>();
    }

    public archimateC3_ArchimateElement(
        String description,        String elementName        ArrayList<archimateC3_ArchimateElement> archimatec3_archimateelements    ) {
        this.description = description;
        this.elementName = elementName;
        this.archimatec3_archimateelements = archimatec3_archimateelements;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }

    public List<archimateC3_ArchimateElement> getArchimatec3_archimateelements() {
        return archimatec3_archimateelements;
    }

    public void addArchimatec3_archimateelement(Archimatec3_archimateelement archimatec3_archimateelement) {
        this.archimatec3_archimateelements.add(archimatec3_archimateelement);
    }
    public archimateC3_ArchimateElement getArchimatec3_archimateelement() {
        return archimatec3_archimateelement;
    }

    public void setArchimatec3_archimateelement(archimateC3_ArchimateElement archimatec3_archimateelement) {
        this.archimatec3_archimateelement = archimatec3_archimateelement;
    }
    public archimateC3_ArchimateModel getArchimatec3_archimatemodel() {
        return archimatec3_archimatemodel;
    }

    public void setArchimatec3_archimatemodel(archimateC3_ArchimateModel archimatec3_archimatemodel) {
        this.archimatec3_archimatemodel = archimatec3_archimatemodel;
    }

}