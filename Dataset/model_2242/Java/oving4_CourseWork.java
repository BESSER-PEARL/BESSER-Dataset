





import java.util.List;
import java.util.ArrayList;

public class oving4_CourseWork  {

    private String name;
    private boolean isMandatory;
    private String type;



    public oving4_CourseWork(
        String name,        boolean isMandatory,        String type    ) {
        this.name = name;
        this.isMandatory = isMandatory;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}