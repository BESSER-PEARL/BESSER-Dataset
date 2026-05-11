





import java.util.List;
import java.util.ArrayList;

public class jpdl32_SwimlaneType  {

    private String name;





    private jpdl32_DocumentRoot jpdl32_documentroot;




    private jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype;




    private jpdl32_AssignmentType jpdl32_assignmenttype;


    public jpdl32_SwimlaneType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public jpdl32_ProcessDefinitionType getJpdl32_processdefinitiontype() {
        return jpdl32_processdefinitiontype;
    }

    public void setJpdl32_processdefinitiontype(jpdl32_ProcessDefinitionType jpdl32_processdefinitiontype) {
        this.jpdl32_processdefinitiontype = jpdl32_processdefinitiontype;
    }
    public jpdl32_AssignmentType getJpdl32_assignmenttype() {
        return jpdl32_assignmenttype;
    }

    public void setJpdl32_assignmenttype(jpdl32_AssignmentType jpdl32_assignmenttype) {
        this.jpdl32_assignmenttype = jpdl32_assignmenttype;
    }

}