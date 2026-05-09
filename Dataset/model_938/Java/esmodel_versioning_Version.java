





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_Version  {






    private Project project;




    private List<versioning_TagVersionSpec> versioning_tagversionspecs;




    private versioning_Version versioning_version;




    private versioning_ChangePackage versioning_changepackage;




    private versioning_Version versioning_version;




    private versioning_PrimaryVersionSpec versioning_primaryversionspec;


    public esmodel_versioning_Version(
    ) {
        this.versioning_tagversionspecs = new ArrayList<>();
    }

    public esmodel_versioning_Version(
        ArrayList<versioning_TagVersionSpec> versioning_tagversionspecs    ) {
        this.versioning_tagversionspecs = versioning_tagversionspecs;
    }


    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }
    public List<versioning_TagVersionSpec> getVersioning_tagversionspecs() {
        return versioning_tagversionspecs;
    }

    public void addVersioning_tagversionspec(Versioning_tagversionspec versioning_tagversionspec) {
        this.versioning_tagversionspecs.add(versioning_tagversionspec);
    }
    public versioning_Version getVersioning_version() {
        return versioning_version;
    }

    public void setVersioning_version(versioning_Version versioning_version) {
        this.versioning_version = versioning_version;
    }
    public versioning_ChangePackage getVersioning_changepackage() {
        return versioning_changepackage;
    }

    public void setVersioning_changepackage(versioning_ChangePackage versioning_changepackage) {
        this.versioning_changepackage = versioning_changepackage;
    }
    public versioning_Version getVersioning_version() {
        return versioning_version;
    }

    public void setVersioning_version(versioning_Version versioning_version) {
        this.versioning_version = versioning_version;
    }
    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }

}