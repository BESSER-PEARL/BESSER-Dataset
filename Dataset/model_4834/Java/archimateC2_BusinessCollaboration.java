





import java.util.List;
import java.util.ArrayList;

public class archimateC2_BusinessCollaboration extends BusinessRole {

    private String collaboration;





    private List<archimateC2_BusinessActor> archimatec2_businessactors;




    private List<archimateC2_BusinessRole> archimatec2_businessroles;




    private archimateC2_BusinessRole archimatec2_businessrole;




    private archimateC2_BusinessActor archimatec2_businessactor;


    public archimateC2_BusinessCollaboration(
        String collaboration    ) {
        super(
        );
        this.collaboration = collaboration;
        this.archimatec2_businessactors = new ArrayList<>();
        this.archimatec2_businessroles = new ArrayList<>();
    }

    public archimateC2_BusinessCollaboration(
        String collaboration        ArrayList<archimateC2_BusinessActor> archimatec2_businessactors,        ArrayList<archimateC2_BusinessRole> archimatec2_businessroles    ) {
        this.collaboration = collaboration;
        this.archimatec2_businessactors = archimatec2_businessactors;
        this.archimatec2_businessroles = archimatec2_businessroles;
    }

    public String getCollaboration() {
        return collaboration;
    }

    public void setCollaboration(String collaboration) {
        this.collaboration = collaboration;
    }

    public List<archimateC2_BusinessActor> getArchimatec2_businessactors() {
        return archimatec2_businessactors;
    }

    public void addArchimatec2_businessactor(Archimatec2_businessactor archimatec2_businessactor) {
        this.archimatec2_businessactors.add(archimatec2_businessactor);
    }
    public List<archimateC2_BusinessRole> getArchimatec2_businessroles() {
        return archimatec2_businessroles;
    }

    public void addArchimatec2_businessrole(Archimatec2_businessrole archimatec2_businessrole) {
        this.archimatec2_businessroles.add(archimatec2_businessrole);
    }
    public archimateC2_BusinessRole getArchimatec2_businessrole() {
        return archimatec2_businessrole;
    }

    public void setArchimatec2_businessrole(archimateC2_BusinessRole archimatec2_businessrole) {
        this.archimatec2_businessrole = archimatec2_businessrole;
    }
    public archimateC2_BusinessActor getArchimatec2_businessactor() {
        return archimatec2_businessactor;
    }

    public void setArchimatec2_businessactor(archimateC2_BusinessActor archimatec2_businessactor) {
        this.archimatec2_businessactor = archimatec2_businessactor;
    }

}