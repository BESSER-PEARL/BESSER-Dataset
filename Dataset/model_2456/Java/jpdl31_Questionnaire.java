





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Questionnaire  {

    private String type;
    private String name;





    private List<jpdl31_ProcessDefinitionType> jpdl31_processdefinitiontypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;


    public jpdl31_Questionnaire(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.jpdl31_processdefinitiontypes = new ArrayList<>();
    }

    public jpdl31_Questionnaire(
        String type,        String name        ArrayList<jpdl31_ProcessDefinitionType> jpdl31_processdefinitiontypes    ) {
        this.type = type;
        this.name = name;
        this.jpdl31_processdefinitiontypes = jpdl31_processdefinitiontypes;
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

    public List<jpdl31_ProcessDefinitionType> getJpdl31_processdefinitiontypes() {
        return jpdl31_processdefinitiontypes;
    }

    public void addJpdl31_processdefinitiontype(Jpdl31_processdefinitiontype jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontypes.add(jpdl31_processdefinitiontype);
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }

}