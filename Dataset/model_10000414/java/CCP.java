





import java.util.List;
import java.util.ArrayList;

public class CCP  {

    private int id_ccp;
    private String label;
    private String description;





    private List<Formation> formations;


    public CCP(
        int id_ccp,        String label,        String description    ) {
        this.id_ccp = id_ccp;
        this.label = label;
        this.description = description;
        this.formations = new ArrayList<>();
    }

    public CCP(
        int id_ccp,        String label,        String description        ArrayList<Formation> formations    ) {
        this.id_ccp = id_ccp;
        this.label = label;
        this.description = description;
        this.formations = formations;
    }

    public int getId_ccp() {
        return id_ccp;
    }

    public void setId_ccp(int id_ccp) {
        this.id_ccp = id_ccp;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Formation> getFormations() {
        return formations;
    }

    public void addFormation(Formation formation) {
        this.formations.add(formation);
    }

}