





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Javadoc extends DocumentationTask {

    private String sourcepath;
    private String defaultexcludes;
    private String use;
    private String version;
    private String packagenames;
    private String author;
    private String windowtitle;
    private String destdir;



    public MavenMaven_Javadoc(
        String sourcepath,        String defaultexcludes,        String use,        String version,        String packagenames,        String author,        String windowtitle,        String destdir    ) {
        super(
        );
        this.sourcepath = sourcepath;
        this.defaultexcludes = defaultexcludes;
        this.use = use;
        this.version = version;
        this.packagenames = packagenames;
        this.author = author;
        this.windowtitle = windowtitle;
        this.destdir = destdir;
    }


    public String getSourcepath() {
        return sourcepath;
    }

    public void setSourcepath(String sourcepath) {
        this.sourcepath = sourcepath;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }
    public String getUse() {
        return use;
    }

    public void setUse(String use) {
        this.use = use;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public String getWindowtitle() {
        return windowtitle;
    }

    public void setWindowtitle(String windowtitle) {
        this.windowtitle = windowtitle;
    }
    public String getDestdir() {
        return destdir;
    }

    public void setDestdir(String destdir) {
        this.destdir = destdir;
    }


}