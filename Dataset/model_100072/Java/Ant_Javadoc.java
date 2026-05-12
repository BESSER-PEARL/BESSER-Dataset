





import java.util.List;
import java.util.ArrayList;

public class Ant_Javadoc extends DocumentationTask {

    private String packagenames;
    private String destdir;
    private String windowtitle;
    private String use;
    private String defaultexcludes;
    private String author;
    private String sourcepath;
    private String version;



    public Ant_Javadoc(
        String packagenames,        String destdir,        String windowtitle,        String use,        String defaultexcludes,        String author,        String sourcepath,        String version    ) {
        super(
        );
        this.packagenames = packagenames;
        this.destdir = destdir;
        this.windowtitle = windowtitle;
        this.use = use;
        this.defaultexcludes = defaultexcludes;
        this.author = author;
        this.sourcepath = sourcepath;
        this.version = version;
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
    public String getWindowtitle() {
        return windowtitle;
    }

    public void setWindowtitle(String windowtitle) {
        this.windowtitle = windowtitle;
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


}