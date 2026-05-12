





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Jar extends ArchiveTask {

    private String basedir;
    private String compress;
    private String jarfile;
    private String encoding;
    private String manifest;



    public MavenMaven_Jar(
        String basedir,        String compress,        String jarfile,        String encoding,        String manifest    ) {
        super(
        );
        this.basedir = basedir;
        this.compress = compress;
        this.jarfile = jarfile;
        this.encoding = encoding;
        this.manifest = manifest;
    }


    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
        this.basedir = basedir;
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


}