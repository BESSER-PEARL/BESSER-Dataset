





import java.util.List;
import java.util.ArrayList;

public class Document  {

    private int id_document;
    private boolean cours;
    private String descriptif;
    private String label;
    private String url;





    private List<Session> sessions;


    public Document(
        int id_document,        boolean cours,        String descriptif,        String label,        String url    ) {
        this.id_document = id_document;
        this.cours = cours;
        this.descriptif = descriptif;
        this.label = label;
        this.url = url;
        this.sessions = new ArrayList<>();
    }

    public Document(
        int id_document,        boolean cours,        String descriptif,        String label,        String url        ArrayList<Session> sessions    ) {
        this.id_document = id_document;
        this.cours = cours;
        this.descriptif = descriptif;
        this.label = label;
        this.url = url;
        this.sessions = sessions;
    }

    public int getId_document() {
        return id_document;
    }

    public void setId_document(int id_document) {
        this.id_document = id_document;
    }
    public boolean getCours() {
        return cours;
    }

    public void setCours(boolean cours) {
        this.cours = cours;
    }
    public String getDescriptif() {
        return descriptif;
    }

    public void setDescriptif(String descriptif) {
        this.descriptif = descriptif;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public List<Session> getSessions() {
        return sessions;
    }

    public void addSession(Session session) {
        this.sessions.add(session);
    }

}