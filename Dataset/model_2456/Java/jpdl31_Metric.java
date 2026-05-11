





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Metric  {

    private String description;
    private String refname;
    private String type;
    private String name;





    private jpdl31_DocumentRoot jpdl31_documentroot;




    private List<jpdl31_ProcessDefinitionType> jpdl31_processdefinitiontypes;


    public jpdl31_Metric(
        String description,        String refname,        String type,        String name    ) {
        this.description = description;
        this.refname = refname;
        this.type = type;
        this.name = name;
        this.jpdl31_processdefinitiontypes = new ArrayList<>();
    }

    public jpdl31_Metric(
        String description,        String refname,        String type,        String name        ArrayList<jpdl31_ProcessDefinitionType> jpdl31_processdefinitiontypes    ) {
        this.description = description;
        this.refname = refname;
        this.type = type;
        this.name = name;
        this.jpdl31_processdefinitiontypes = jpdl31_processdefinitiontypes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRefname() {
        return refname;
    }

    public void setRefname(String refname) {
        this.refname = refname;
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

    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public List<jpdl31_ProcessDefinitionType> getJpdl31_processdefinitiontypes() {
        return jpdl31_processdefinitiontypes;
    }

    public void addJpdl31_processdefinitiontype(Jpdl31_processdefinitiontype jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontypes.add(jpdl31_processdefinitiontype);
    }

}