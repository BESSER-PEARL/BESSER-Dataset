





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_AntTaskDef extends ContentsGoal {

    private String name;
    private String classname;



    public MavenMaven_AntTaskDef(
        String name,        String classname    ) {
        super(
        );
        this.name = name;
        this.classname = classname;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }


}