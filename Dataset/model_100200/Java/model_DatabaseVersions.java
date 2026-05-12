





import java.util.List;
import java.util.ArrayList;

public class model_DatabaseVersions  {

    private String fileName;
    private String packageName;





    private List<model_DatabaseVersion> model_databaseversions;


    public model_DatabaseVersions(
        String fileName,        String packageName    ) {
        this.fileName = fileName;
        this.packageName = packageName;
        this.model_databaseversions = new ArrayList<>();
    }

    public model_DatabaseVersions(
        String fileName,        String packageName        ArrayList<model_DatabaseVersion> model_databaseversions    ) {
        this.fileName = fileName;
        this.packageName = packageName;
        this.model_databaseversions = model_databaseversions;
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

    public List<model_DatabaseVersion> getModel_databaseversions() {
        return model_databaseversions;
    }

    public void addModel_databaseversion(Model_databaseversion model_databaseversion) {
        this.model_databaseversions.add(model_databaseversion);
    }

}