





import java.util.List;
import java.util.ArrayList;

public class model_DatabaseVersions  {

    private String fileName;
    private String packageName;



    public model_DatabaseVersions(
        String fileName,        String packageName    ) {
        this.fileName = fileName;
        this.packageName = packageName;
    }


    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }


}