





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_HistoryInfo  {






    private versioning_LogMessage versioning_logmessage;




    private List<versioning_VersionProperty> versioning_versionpropertys;


    public esmodel_versioning_HistoryInfo(
    ) {
        this.versioning_versionpropertys = new ArrayList<>();
    }

    public esmodel_versioning_HistoryInfo(
        ArrayList<versioning_VersionProperty> versioning_versionpropertys    ) {
        this.versioning_versionpropertys = versioning_versionpropertys;
    }


    public versioning_LogMessage getVersioning_logmessage() {
        return versioning_logmessage;
    }

    public void setVersioning_logmessage(versioning_LogMessage versioning_logmessage) {
        this.versioning_logmessage = versioning_logmessage;
    }
    public List<versioning_VersionProperty> getVersioning_versionpropertys() {
        return versioning_versionpropertys;
    }

    public void addVersioning_versionproperty(Versioning_versionproperty versioning_versionproperty) {
        this.versioning_versionpropertys.add(versioning_versionproperty);
    }

}