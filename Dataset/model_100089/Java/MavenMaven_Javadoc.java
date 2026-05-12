





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Javadoc extends DocumentationTask {

    private String windowtitle;
    private String sourcepath;
    private String version;
    private String use;
    private String defaultexcludes;
    private String author;
    private String packagenames;
    private String destdir;



    public MavenMaven_Javadoc(
        String windowtitle,        String sourcepath,        String version,        String use,        String defaultexcludes,        String author,        String packagenames,        String destdir    ) {
        super(
        );
        this.windowtitle = windowtitle;
        this.sourcepath = sourcepath;
        this.version = version;
        this.use = use;
        this.defaultexcludes = defaultexcludes;
        this.author = author;
        this.packagenames = packagenames;
        this.destdir = destdir;
    }


    public String getWindowtitle() {
        return windowtitle;
    }

    public void setWindowtitle(String windowtitle) {
        this.windowtitle = windowtitle;
    }
    public String getSourcepath() {
        return sourcepath;
    }

    public void setSourcepath(String sourcepath) {
        this.sourcepath = sourcepath;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getUse() {
        return use;
    }

    public void setUse(String use) {
        this.use = use;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getPackagenames() {
        return packagenames;
    }

    public void setPackagenames(String packagenames) {
        this.packagenames = packagenames;
    }
    public String getDestdir() {
        return destdir;
    }

    public void setDestdir(String destdir) {
        this.destdir = destdir;
    }


}