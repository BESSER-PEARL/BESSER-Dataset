





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Mapper extends Basic {

    private String type;
    private String classpathref;
    private String classname;
    private String to;
    private String from_;
    private String classpath;



    public MavenMaven_Mapper(
        String type,        String classpathref,        String classname,        String to,        String from_,        String classpath    ) {
        super(
        );
        this.type = type;
        this.classpathref = classpathref;
        this.classname = classname;
        this.to = to;
        this.from_ = from_;
        this.classpath = classpath;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getClasspathref() {
        return classpathref;
    }

    public void setClasspathref(String classpathref) {
        this.classpathref = classpathref;
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
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getClasspath() {
        return classpath;
    }

    public void setClasspath(String classpath) {
        this.classpath = classpath;
    }


}