





import java.util.List;
import java.util.ArrayList;

public class model_DatabaseVersions  {

    private String packageName;
    private String fileName;



    public model_DatabaseVersions(
        String packageName,        String fileName    ) {
        this.packageName = packageName;
        this.fileName = fileName;
    }


    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }


}