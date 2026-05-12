





import java.util.List;
import java.util.ArrayList;

public class Ant_Javadoc extends DocumentationTask {

    private String version;
    private String packagenames;
    private String sourcepath;
    private String destdir;
    private String use;
    private String windowtitle;
    private String author;
    private String defaultexcludes;



    public Ant_Javadoc(
        String version,        String packagenames,        String sourcepath,        String destdir,        String use,        String windowtitle,        String author,        String defaultexcludes    ) {
        super(
        );
        this.version = version;
        this.packagenames = packagenames;
        this.sourcepath = sourcepath;
        this.destdir = destdir;
        this.use = use;
        this.windowtitle = windowtitle;
        this.author = author;
        this.defaultexcludes = defaultexcludes;
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
    public String getWindowtitle() {
        return windowtitle;
    }

    public void setWindowtitle(String windowtitle) {
        this.windowtitle = windowtitle;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getDefaultexcludes() {
        return defaultexcludes;
    }

    public void setDefaultexcludes(String defaultexcludes) {
        this.defaultexcludes = defaultexcludes;
    }


}