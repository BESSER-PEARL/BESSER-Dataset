





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Artefact  {

    private String name;
    private String description;
    private String type;





    private jpdl31_TaskNodeType jpdl31_tasknodetype;




    private jpdl31_TaskType jpdl31_tasktype;


    public jpdl31_Artefact(
        String name,        String description,        String type    ) {
        this.name = name;
        this.description = description;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public jpdl31_TaskNodeType getJpdl31_tasknodetype() {
        return jpdl31_tasknodetype;
    }

    public void setJpdl31_tasknodetype(jpdl31_TaskNodeType jpdl31_tasknodetype) {
        this.jpdl31_tasknodetype = jpdl31_tasknodetype;
    }
    public jpdl31_TaskType getJpdl31_tasktype() {
        return jpdl31_tasktype;
    }

    public void setJpdl31_tasktype(jpdl31_TaskType jpdl31_tasktype) {
        this.jpdl31_tasktype = jpdl31_tasktype;
    }

}