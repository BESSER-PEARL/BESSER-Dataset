





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_HistoryInfo  {






    private List<versioning_VersionProperty> versioning_versionpropertys;




    private List<versioning_TagVersionSpec> versioning_tagversionspecs;




    private versioning_PrimaryVersionSpec versioning_primaryversionspec;




    private versioning_ChangePackage versioning_changepackage;




    private versioning_LogMessage versioning_logmessage;


    public esmodel_versioning_HistoryInfo(
    ) {
        this.versioning_versionpropertys = new ArrayList<>();
        this.versioning_tagversionspecs = new ArrayList<>();
    }

    public esmodel_versioning_HistoryInfo(
        ArrayList<versioning_VersionProperty> versioning_versionpropertys,        ArrayList<versioning_TagVersionSpec> versioning_tagversionspecs    ) {
        this.versioning_versionpropertys = versioning_versionpropertys;
        this.versioning_tagversionspecs = versioning_tagversionspecs;
    }


    public List<versioning_VersionProperty> getVersioning_versionpropertys() {
        return versioning_versionpropertys;
    }

    public void addVersioning_versionproperty(Versioning_versionproperty versioning_versionproperty) {
        this.versioning_versionpropertys.add(versioning_versionproperty);
    }
    public List<versioning_TagVersionSpec> getVersioning_tagversionspecs() {
        return versioning_tagversionspecs;
    }

    public void addVersioning_tagversionspec(Versioning_tagversionspec versioning_tagversionspec) {
        this.versioning_tagversionspecs.add(versioning_tagversionspec);
    }
    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }
    public versioning_ChangePackage getVersioning_changepackage() {
        return versioning_changepackage;
    }

    public void setVersioning_changepackage(versioning_ChangePackage versioning_changepackage) {
        this.versioning_changepackage = versioning_changepackage;
    }
    public versioning_LogMessage getVersioning_logmessage() {
        return versioning_logmessage;
    }

    public void setVersioning_logmessage(versioning_LogMessage versioning_logmessage) {
        this.versioning_logmessage = versioning_logmessage;
    }

}