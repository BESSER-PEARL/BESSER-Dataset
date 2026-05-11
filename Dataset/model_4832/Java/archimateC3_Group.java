





import java.util.List;
import java.util.ArrayList;

public class archimateC3_Group  {

    private String groupName;





    private List<archimateC3_ArchimateElement> archimatec3_archimateelements;




    private archimateC3_ArchimateModel archimatec3_archimatemodel;


    public archimateC3_Group(
        String groupName    ) {
        this.groupName = groupName;
        this.archimatec3_archimateelements = new ArrayList<>();
    }

    public archimateC3_Group(
        String groupName        ArrayList<archimateC3_ArchimateElement> archimatec3_archimateelements    ) {
        this.groupName = groupName;
        this.archimatec3_archimateelements = archimatec3_archimateelements;
    }

    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
    }

    public List<archimateC3_ArchimateElement> getArchimatec3_archimateelements() {
        return archimatec3_archimateelements;
    }

    public void addArchimatec3_archimateelement(Archimatec3_archimateelement archimatec3_archimateelement) {
        this.archimatec3_archimateelements.add(archimatec3_archimateelement);
    }
    public archimateC3_ArchimateModel getArchimatec3_archimatemodel() {
        return archimatec3_archimatemodel;
    }

    public void setArchimatec3_archimatemodel(archimateC3_ArchimateModel archimatec3_archimatemodel) {
        this.archimatec3_archimatemodel = archimatec3_archimatemodel;
    }

}