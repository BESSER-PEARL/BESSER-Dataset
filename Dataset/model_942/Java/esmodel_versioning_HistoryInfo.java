





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_HistoryInfo  {






    private List<versioning_VersionProperty> versioning_versionpropertys;




    private versioning_PrimaryVersionSpec versioning_primaryversionspec;


    public esmodel_versioning_HistoryInfo(
    ) {
        this.versioning_versionpropertys = new ArrayList<>();
    }

    public esmodel_versioning_HistoryInfo(
        ArrayList<versioning_VersionProperty> versioning_versionpropertys    ) {
        this.versioning_versionpropertys = versioning_versionpropertys;
    }


    public List<versioning_VersionProperty> getVersioning_versionpropertys() {
        return versioning_versionpropertys;
    }

    public void addVersioning_versionproperty(Versioning_versionproperty versioning_versionproperty) {
        this.versioning_versionpropertys.add(versioning_versionproperty);
    }
    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }

}