





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_ChangePackage  {






    private List<versioning_VersionProperty> versioning_versionpropertys;


    public esmodel_versioning_ChangePackage(
    ) {
        this.versioning_versionpropertys = new ArrayList<>();
    }

    public esmodel_versioning_ChangePackage(
        ArrayList<versioning_VersionProperty> versioning_versionpropertys    ) {
        this.versioning_versionpropertys = versioning_versionpropertys;
    }


    public List<versioning_VersionProperty> getVersioning_versionpropertys() {
        return versioning_versionpropertys;
    }

    public void addVersioning_versionproperty(Versioning_versionproperty versioning_versionproperty) {
        this.versioning_versionpropertys.add(versioning_versionproperty);
    }

}