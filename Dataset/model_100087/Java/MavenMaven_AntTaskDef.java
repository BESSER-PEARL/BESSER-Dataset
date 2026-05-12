





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_AntTaskDef extends ContentsGoal {

    private String classname;
    private String name;



    public MavenMaven_AntTaskDef(
        String classname,        String name    ) {
        super(
        );
        this.classname = classname;
        this.name = name;
    }


    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}