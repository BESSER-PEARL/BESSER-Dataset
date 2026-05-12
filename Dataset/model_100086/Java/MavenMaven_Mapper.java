





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Mapper extends Basic {

    private String classpathref;
    private String to;
    private String from_;
    private String type;
    private String classname;
    private String classpath;



    public MavenMaven_Mapper(
        String classpathref,        String to,        String from_,        String type,        String classname,        String classpath    ) {
        super(
        );
        this.classpathref = classpathref;
        this.to = to;
        this.from_ = from_;
        this.type = type;
        this.classname = classname;
        this.classpath = classpath;
    }


    public String getClasspathref() {
        return classpathref;
    }

    public void setClasspathref(String classpathref) {
        this.classpathref = classpathref;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
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
    public String getClasspath() {
        return classpath;
    }

    public void setClasspath(String classpath) {
        this.classpath = classpath;
    }


}