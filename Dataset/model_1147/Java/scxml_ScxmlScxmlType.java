





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlScxmlType  {

    private String version;
    private String initial;
    private String id;





    private List<scxml_ScxmlScriptType> scxml_scxmlscripttypes;


    public scxml_ScxmlScxmlType(
        String version,        String initial,        String id    ) {
        this.version = version;
        this.initial = initial;
        this.id = id;
        this.scxml_scxmlscripttypes = new ArrayList<>();
    }

    public scxml_ScxmlScxmlType(
        String version,        String initial,        String id        ArrayList<scxml_ScxmlScriptType> scxml_scxmlscripttypes    ) {
        this.version = version;
        this.initial = initial;
        this.id = id;
        this.scxml_scxmlscripttypes = scxml_scxmlscripttypes;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getInitial() {
        return initial;
    }

    public void setInitial(String initial) {
        this.initial = initial;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<scxml_ScxmlScriptType> getScxml_scxmlscripttypes() {
        return scxml_scxmlscripttypes;
    }

    public void addScxml_scxmlscripttype(Scxml_scxmlscripttype scxml_scxmlscripttype) {
        this.scxml_scxmlscripttypes.add(scxml_scxmlscripttype);
    }

}