





import java.util.List;
import java.util.ArrayList;

public class Ant_Jar extends ArchiveTask {

    private String basedir;
    private String jarfile;
    private String compress;
    private String manifest;
    private String encoding;



    public Ant_Jar(
        String basedir,        String jarfile,        String compress,        String manifest,        String encoding    ) {
        super(
        );
        this.basedir = basedir;
        this.jarfile = jarfile;
        this.compress = compress;
        this.manifest = manifest;
        this.encoding = encoding;
    }


    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
        this.basedir = basedir;
    }
    public String getJarfile() {
        return jarfile;
    }

    public void setJarfile(String jarfile) {
        this.jarfile = jarfile;
    }
    public String getCompress() {
        return compress;
    }

    public void setCompress(String compress) {
        this.compress = compress;
    }
    public String getManifest() {
        return manifest;
    }

    public void setManifest(String manifest) {
        this.manifest = manifest;
    }
    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }


}