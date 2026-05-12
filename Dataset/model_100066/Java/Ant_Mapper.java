





import java.util.List;
import java.util.ArrayList;

public class Ant_Mapper extends Basic {

    private String from_;
    private String to;
    private String type;
    private String classname;
    private String classpathref;
    private String classpath;



    public Ant_Mapper(
        String from_,        String to,        String type,        String classname,        String classpathref,        String classpath    ) {
        super(
        );
        this.from_ = from_;
        this.to = to;
        this.type = type;
        this.classname = classname;
        this.classpathref = classpathref;
        this.classpath = classpath;
    }


    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getClasspathref() {
        return classpathref;
    }

    public void setClasspathref(String classpathref) {
        this.classpathref = classpathref;
    }
    public String getClasspath() {
        return classpath;
    }

    public void setClasspath(String classpath) {
        this.classpath = classpath;
    }


}