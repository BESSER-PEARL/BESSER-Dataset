





import java.util.List;
import java.util.ArrayList;

public class eJSL_PositionParameter  {

    private String type;
    private String name;
    private String divid;





    private List<eJSL_KeyValuePair> ejsl_keyvaluepairs;




    private eJSL_Position ejsl_position;


    public eJSL_PositionParameter(
        String type,        String name,        String divid    ) {
        this.type = type;
        this.name = name;
        this.divid = divid;
        this.ejsl_keyvaluepairs = new ArrayList<>();
    }

    public eJSL_PositionParameter(
        String type,        String name,        String divid        ArrayList<eJSL_KeyValuePair> ejsl_keyvaluepairs    ) {
        this.type = type;
        this.name = name;
        this.divid = divid;
        this.ejsl_keyvaluepairs = ejsl_keyvaluepairs;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDivid() {
        return divid;
    }

    public void setDivid(String divid) {
        this.divid = divid;
    }

    public List<eJSL_KeyValuePair> getEjsl_keyvaluepairs() {
        return ejsl_keyvaluepairs;
    }

    public void addEjsl_keyvaluepair(Ejsl_keyvaluepair ejsl_keyvaluepair) {
        this.ejsl_keyvaluepairs.add(ejsl_keyvaluepair);
    }
    public eJSL_Position getEjsl_position() {
        return ejsl_position;
    }

    public void setEjsl_position(eJSL_Position ejsl_position) {
        this.ejsl_position = ejsl_position;
    }

}