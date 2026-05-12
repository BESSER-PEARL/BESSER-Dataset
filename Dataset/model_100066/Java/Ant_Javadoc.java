





import java.util.List;
import java.util.ArrayList;

public class Ant_Javadoc extends DocumentationTask {

    private String author;
    private String version;
    private String windowtitle;
    private String destdir;
    private String packagenames;
    private String use;
    private String sourcepath;
    private String defaultexcludes;



    public Ant_Javadoc(
        String author,        String version,        String windowtitle,        String destdir,        String packagenames,        String use,        String sourcepath,        String defaultexcludes    ) {
        super(
        );
        this.author = author;
        this.version = version;
        this.windowtitle = windowtitle;
        this.destdir = destdir;
        this.packagenames = packagenames;
        this.use = use;
        this.sourcepath = sourcepath;
        this.defaultexcludes = defaultexcludes;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public String getPackagenames() {
        return packagenames;
    }

    public void setPackagenames(String packagenames) {
        this.packagenames = packagenames;
    }
    public String getUse() {
        return use;
    }

    public void setUse(String use) {
        this.use = use;
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


}