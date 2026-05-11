





import java.util.List;
import java.util.ArrayList;

public class jpdl31_SwimlaneType  {

    private String name;





    private jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private jpdl31_AssignmentType jpdl31_assignmenttype;


    public jpdl31_SwimlaneType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl31_ProcessDefinitionType getJpdl31_processdefinitiontype() {
        return jpdl31_processdefinitiontype;
    }

    public void setJpdl31_processdefinitiontype(jpdl31_ProcessDefinitionType jpdl31_processdefinitiontype) {
        this.jpdl31_processdefinitiontype = jpdl31_processdefinitiontype;
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public jpdl31_AssignmentType getJpdl31_assignmenttype() {
        return jpdl31_assignmenttype;
    }

    public void setJpdl31_assignmenttype(jpdl31_AssignmentType jpdl31_assignmenttype) {
        this.jpdl31_assignmenttype = jpdl31_assignmenttype;
    }

}