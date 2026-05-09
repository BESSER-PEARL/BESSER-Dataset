





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_HistoryQuery  {

    private boolean includeChangePackage;





    private versioning_PrimaryVersionSpec versioning_primaryversionspec;




    private versioning_PrimaryVersionSpec versioning_primaryversionspec;




    private List<ModelElementId> modelelementids;


    public esmodel_versioning_HistoryQuery(
        boolean includeChangePackage    ) {
        this.includeChangePackage = includeChangePackage;
        this.modelelementids = new ArrayList<>();
    }

    public esmodel_versioning_HistoryQuery(
        boolean includeChangePackage        ArrayList<ModelElementId> modelelementids    ) {
        this.includeChangePackage = includeChangePackage;
        this.modelelementids = modelelementids;
    }

    public boolean getIncludechangepackage() {
        return includeChangePackage;
    }

    public void setIncludechangepackage(boolean includeChangePackage) {
        this.includeChangePackage = includeChangePackage;
    }

    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }
    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }
    public List<ModelElementId> getModelelementids() {
        return modelelementids;
    }

    public void addModelelementid(Modelelementid modelelementid) {
        this.modelelementids.add(modelelementid);
    }

}