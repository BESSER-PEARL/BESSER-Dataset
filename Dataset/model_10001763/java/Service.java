





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String description;





    private Association association;




    private List<Membre> membres;


    public Service(
        String description    ) {
        this.description = description;
        this.membres = new ArrayList<>();
    }

    public Service(
        String description        ArrayList<Membre> membres    ) {
        this.description = description;
        this.membres = membres;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Association getAssociation() {
        return association;
    }

    public void setAssociation(Association association) {
        this.association = association;
    }
    public List<Membre> getMembres() {
        return membres;
    }

    public void addMembre(Membre membre) {
        this.membres.add(membre);
    }

}