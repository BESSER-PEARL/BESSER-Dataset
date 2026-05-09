





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_Version  {






    private Project project;




    private versioning_LogMessage versioning_logmessage;




    private List<versioning_TagVersionSpec> versioning_tagversionspecs;


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
    public versioning_LogMessage getVersioning_logmessage() {
        return versioning_logmessage;
    }

    public void setVersioning_logmessage(versioning_LogMessage versioning_logmessage) {
        this.versioning_logmessage = versioning_logmessage;
    }
    public List<versioning_TagVersionSpec> getVersioning_tagversionspecs() {
        return versioning_tagversionspecs;
    }

    public void addVersioning_tagversionspec(Versioning_tagversionspec versioning_tagversionspec) {
        this.versioning_tagversionspecs.add(versioning_tagversionspec);
    }

}