





import java.util.List;
import java.util.ArrayList;

public class build_Config  {

    private String archiveFormat;
    private String ws;
    private String arch;
    private String os;





    private build_Platform build_platform;


    public build_Config(
        String archiveFormat,        String ws,        String arch,        String os    ) {
        this.archiveFormat = archiveFormat;
        this.ws = ws;
        this.arch = arch;
        this.os = os;
    }


    public String getArchiveformat() {
        return archiveFormat;
    }

    public void setArchiveformat(String archiveFormat) {
        this.archiveFormat = archiveFormat;
    }
    public String getWs() {
        return ws;
    }

    public void setWs(String ws) {
        this.ws = ws;
    }
    public String getArch() {
        return arch;
    }

    public void setArch(String arch) {
        this.arch = arch;
    }
    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }

    public build_Platform getBuild_platform() {
        return build_platform;
    }

    public void setBuild_platform(build_Platform build_platform) {
        this.build_platform = build_platform;
    }

}