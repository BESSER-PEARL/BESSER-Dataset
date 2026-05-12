





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Jar extends ArchiveTask {

    private String manifest;
    private String basedir;
    private String encoding;
    private String compress;
    private String jarfile;



    public MavenMaven_Jar(
        String manifest,        String basedir,        String encoding,        String compress,        String jarfile    ) {
        super(
        );
        this.manifest = manifest;
        this.basedir = basedir;
        this.encoding = encoding;
        this.compress = compress;
        this.jarfile = jarfile;
    }


    public String getManifest() {
        return manifest;
    }

    public void setManifest(String manifest) {
        this.manifest = manifest;
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