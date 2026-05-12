





import java.util.List;
import java.util.ArrayList;

public class Formation  {

    private int id_formation;
    private String label;
    private String descriptif;





    private List<Session> sessions;


    public Formation(
        int id_formation,        String label,        String descriptif    ) {
        this.id_formation = id_formation;
        this.label = label;
        this.descriptif = descriptif;
        this.sessions = new ArrayList<>();
    }

    public Formation(
        int id_formation,        String label,        String descriptif        ArrayList<Session> sessions    ) {
        this.id_formation = id_formation;
        this.label = label;
        this.descriptif = descriptif;
        this.sessions = sessions;
    }

    public int getId_formation() {
        return id_formation;
    }

    public void setId_formation(int id_formation) {
        this.id_formation = id_formation;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDescriptif() {
        return descriptif;
    }

    public void setDescriptif(String descriptif) {
        this.descriptif = descriptif;
    }

    public List<Session> getSessions() {
        return sessions;
    }

    public void addSession(Session session) {
        this.sessions.add(session);
    }

}