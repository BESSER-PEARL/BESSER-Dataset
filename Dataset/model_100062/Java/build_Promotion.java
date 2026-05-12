





import java.util.List;
import java.util.ArrayList;

public class build_Promotion  {

    private String buildAlias;
    private boolean incubating;
    private String downloadDirectory;
    private String baseURL;
    private String uploadDirectory;



    public build_Promotion(
        String buildAlias,        boolean incubating,        String downloadDirectory,        String baseURL,        String uploadDirectory    ) {
        this.buildAlias = buildAlias;
        this.incubating = incubating;
        this.downloadDirectory = downloadDirectory;
        this.baseURL = baseURL;
        this.uploadDirectory = uploadDirectory;
    }


    public String getBuildalias() {
        return buildAlias;
    }

    public void setBuildalias(String buildAlias) {
        this.buildAlias = buildAlias;
    }
    public boolean getIncubating() {
        return incubating;
    }

    public void setIncubating(boolean incubating) {
        this.incubating = incubating;
    }
    public String getDownloaddirectory() {
        return downloadDirectory;
    }

    public void setDownloaddirectory(String downloadDirectory) {
        this.downloadDirectory = downloadDirectory;
    }
    public String getBaseurl() {
        return baseURL;
    }

    public void setBaseurl(String baseURL) {
        this.baseURL = baseURL;
    }
    public String getUploaddirectory() {
        return uploadDirectory;
    }

    public void setUploaddirectory(String uploadDirectory) {
        this.uploadDirectory = uploadDirectory;
    }


}