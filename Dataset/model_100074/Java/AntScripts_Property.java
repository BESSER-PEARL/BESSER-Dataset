





import java.util.List;
import java.util.ArrayList;

public class AntScripts_Property  {

    private String classpathref;
    private String environment;
    private String file;
    private String resource;
    private String value;
    private String classpath;
    private String location;
    private String refid;
    private String name;
    private String url;
    private String prefix;



    public AntScripts_Property(
        String classpathref,        String environment,        String file,        String resource,        String value,        String classpath,        String location,        String refid,        String name,        String url,        String prefix    ) {
        this.classpathref = classpathref;
        this.environment = environment;
        this.file = file;
        this.resource = resource;
        this.value = value;
        this.classpath = classpath;
        this.location = location;
        this.refid = refid;
        this.name = name;
        this.url = url;
        this.prefix = prefix;
    }


    public String getClasspathref() {
        return classpathref;
    }

    public void setClasspathref(String classpathref) {
        this.classpathref = classpathref;
    }
    public String getEnvironment() {
        return environment;
    }

    public void setEnvironment(String environment) {
        this.environment = environment;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getClasspath() {
        return classpath;
    }

    public void setClasspath(String classpath) {
        this.classpath = classpath;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getRefid() {
        return refid;
    }

    public void setRefid(String refid) {
        this.refid = refid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}