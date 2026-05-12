





import java.util.List;
import java.util.ArrayList;

public class Ant_Mapper extends Basic {

    private String type;
    private String classpath;
    private String classname;
    private String to;
    private String classpathref;
    private String from_;



    public Ant_Mapper(
        String type,        String classpath,        String classname,        String to,        String classpathref,        String from_    ) {
        super(
        );
        this.type = type;
        this.classpath = classpath;
        this.classname = classname;
        this.to = to;
        this.classpathref = classpathref;
        this.from_ = from_;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getClasspath() {
        return classpath;
    }

    public void setClasspath(String classpath) {
        this.classpath = classpath;
    }
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getClasspathref() {
        return classpathref;
    }

    public void setClasspathref(String classpathref) {
        this.classpathref = classpathref;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }


}