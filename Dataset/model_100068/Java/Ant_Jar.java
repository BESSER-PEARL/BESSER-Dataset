





import java.util.List;
import java.util.ArrayList;

public class Ant_Jar extends ArchiveTask {

    private String basedir;
    private String encoding;
    private String manifest;
    private String compress;
    private String jarfile;



    public Ant_Jar(
        String basedir,        String encoding,        String manifest,        String compress,        String jarfile    ) {
        super(
        );
        this.basedir = basedir;
        this.encoding = encoding;
        this.manifest = manifest;
        this.compress = compress;
        this.jarfile = jarfile;
    }


    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
        this.basedir = basedir;
    }
    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }
    public String getManifest() {
        return manifest;
    }

    public void setManifest(String manifest) {
        this.manifest = manifest;
    }
    public String getCompress() {
        return compress;
    }

    public void setCompress(String compress) {
        this.compress = compress;
    }
    public String getJarfile() {
        return jarfile;
    }

    public void setJarfile(String jarfile) {
        this.jarfile = jarfile;
    }


}