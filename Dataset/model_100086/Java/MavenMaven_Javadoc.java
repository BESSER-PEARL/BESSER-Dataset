





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Javadoc extends DocumentationTask {

    private String windowtitle;
    private String version;
    private String defaultexcludes;
    private String sourcepath;
    private String destdir;
    private String use;
    private String packagenames;
    private String author;



    public MavenMaven_Javadoc(
        String windowtitle,        String version,        String defaultexcludes,        String sourcepath,        String destdir,        String use,        String packagenames,        String author    ) {
        super(
        );
        this.windowtitle = windowtitle;
        this.version = version;
        this.defaultexcludes = defaultexcludes;
        this.sourcepath = sourcepath;
        this.destdir = destdir;
        this.use = use;
        this.packagenames = packagenames;
        this.author = author;
    }


    public String getWindowtitle() {
        return windowtitle;
    }

    public void setWindowtitle(String windowtitle) {
        this.windowtitle = windowtitle;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getSourcepath() {
        return sourcepath;
    }

    public void setSourcepath(String sourcepath) {
        this.sourcepath = sourcepath;
    }
    public String getDestdir() {
        return destdir;
    }

    public void setDestdir(String destdir) {
        this.destdir = destdir;
    }
    public String getUse() {
        return use;
    }

    public void setUse(String use) {
        this.use = use;
    }
    public String getPackagenames() {
        return packagenames;
    }

    public void setPackagenames(String packagenames) {
        this.packagenames = packagenames;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


}