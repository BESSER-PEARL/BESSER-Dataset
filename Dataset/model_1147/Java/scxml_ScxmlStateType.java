





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlStateType  {

    private String id;
    private String initial;





    private scxml_ScxmlStateType scxml_scxmlstatetype;




    private List<scxml_ScxmlOnexecuteType> scxml_scxmlonexecutetypes;




    private List<scxml_ScxmlOnexecuteType> scxml_scxmlonexecutetypes;




    private scxml_ScxmlScxmlType scxml_scxmlscxmltype;


    public scxml_ScxmlStateType(
        String id,        String initial    ) {
        this.id = id;
        this.initial = initial;
        this.scxml_scxmlonexecutetypes = new ArrayList<>();
        this.scxml_scxmlonexecutetypes = new ArrayList<>();
    }

    public scxml_ScxmlStateType(
        String id,        String initial        ArrayList<scxml_ScxmlOnexecuteType> scxml_scxmlonexecutetypes,        ArrayList<scxml_ScxmlOnexecuteType> scxml_scxmlonexecutetypes    ) {
        this.id = id;
        this.initial = initial;
        this.scxml_scxmlonexecutetypes = scxml_scxmlonexecutetypes;
        this.scxml_scxmlonexecutetypes = scxml_scxmlonexecutetypes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getInitial() {
        return initial;
    }

    public void setInitial(String initial) {
        this.initial = initial;
    }

    public scxml_ScxmlStateType getScxml_scxmlstatetype() {
        return scxml_scxmlstatetype;
    }

    public void setScxml_scxmlstatetype(scxml_ScxmlStateType scxml_scxmlstatetype) {
        this.scxml_scxmlstatetype = scxml_scxmlstatetype;
    }
    public List<scxml_ScxmlOnexecuteType> getScxml_scxmlonexecutetypes() {
        return scxml_scxmlonexecutetypes;
    }

    public void addScxml_scxmlonexecutetype(Scxml_scxmlonexecutetype scxml_scxmlonexecutetype) {
        this.scxml_scxmlonexecutetypes.add(scxml_scxmlonexecutetype);
    }
    public List<scxml_ScxmlOnexecuteType> getScxml_scxmlonexecutetypes() {
        return scxml_scxmlonexecutetypes;
    }

    public void addScxml_scxmlonexecutetype(Scxml_scxmlonexecutetype scxml_scxmlonexecutetype) {
        this.scxml_scxmlonexecutetypes.add(scxml_scxmlonexecutetype);
    }
    public scxml_ScxmlScxmlType getScxml_scxmlscxmltype() {
        return scxml_scxmlscxmltype;
    }

    public void setScxml_scxmlscxmltype(scxml_ScxmlScxmlType scxml_scxmlscxmltype) {
        this.scxml_scxmlscxmltype = scxml_scxmlscxmltype;
    }

}