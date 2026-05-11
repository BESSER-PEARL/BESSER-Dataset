





import java.util.List;
import java.util.ArrayList;

public class configDsl_Config  {

    private String appName;
    private String outFolder;
    private String srcFolder;
    private String mainClass;



    public configDsl_Config(
        String appName,        String outFolder,        String srcFolder,        String mainClass    ) {
        this.appName = appName;
        this.outFolder = outFolder;
        this.srcFolder = srcFolder;
        this.mainClass = mainClass;
    }


    public String getAppname() {
        return appName;
    }

    public void setAppname(String appName) {
        this.appName = appName;
    }
    public String getOutfolder() {
        return outFolder;
    }

    public void setOutfolder(String outFolder) {
        this.outFolder = outFolder;
    }
    public String getSrcfolder() {
        return srcFolder;
    }

    public void setSrcfolder(String srcFolder) {
        this.srcFolder = srcFolder;
    }
    public String getMainclass() {
        return mainClass;
    }

    public void setMainclass(String mainClass) {
        this.mainClass = mainClass;
    }


}