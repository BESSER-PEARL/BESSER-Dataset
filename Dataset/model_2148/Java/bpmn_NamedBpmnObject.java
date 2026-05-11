





import java.util.List;
import java.util.ArrayList;

public class bpmn_NamedBpmnObject  {

    private String name;
    private String documentation;
    private String ncname;



    public bpmn_NamedBpmnObject(
        String name,        String documentation,        String ncname    ) {
        this.name = name;
        this.documentation = documentation;
        this.ncname = ncname;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getNcname() {
        return ncname;
    }

    public void setNcname(String ncname) {
        this.ncname = ncname;
    }


}