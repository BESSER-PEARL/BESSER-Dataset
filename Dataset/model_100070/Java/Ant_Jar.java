





import java.util.List;
import java.util.ArrayList;

public class Ant_Jar extends ArchiveTask {

    private String encoding;
    private String compress;
    private String basedir;
    private String manifest;
    private String jarfile;



    public Ant_Jar(
        String encoding,        String compress,        String basedir,        String manifest,        String jarfile    ) {
        super(
        );
        this.encoding = encoding;
        this.compress = compress;
        this.basedir = basedir;
        this.manifest = manifest;
        this.jarfile = jarfile;
    }


    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }
    public String getCompress() {
        return compress;
    }

    public void setCompress(String compress) {
        this.compress = compress;
    }
    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
        this.basedir = basedir;
    }
    public String getManifest() {
        return manifest;
    }

    public void setManifest(String manifest) {
        this.manifest = manifest;
    }
    public String getJarfile() {
        return jarfile;
    }

    public void setJarfile(String jarfile) {
        this.jarfile = jarfile;
    }


}