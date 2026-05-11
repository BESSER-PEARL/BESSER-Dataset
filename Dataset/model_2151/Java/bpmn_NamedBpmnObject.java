





import java.util.List;
import java.util.ArrayList;

public class bpmn_NamedBpmnObject  {

    private String documentation;
    private String name;
    private String ncname;



    public bpmn_NamedBpmnObject(
        String documentation,        String name,        String ncname    ) {
        this.documentation = documentation;
        this.name = name;
        this.ncname = ncname;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNcname() {
        return ncname;
    }

    public void setNcname(String ncname) {
        this.ncname = ncname;
    }


}