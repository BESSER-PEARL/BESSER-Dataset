





import java.util.List;
import java.util.ArrayList;

public class jsflibraryregistry_JSFLibrary  {

    private boolean Implementation;
    private boolean Deployed;
    private String Name;
    private String ID;
    private String JSFVersion;





    private List<jsflibraryregistry_ArchiveFile> jsflibraryregistry_archivefiles;




    private jsflibraryregistry_JSFLibraryRegistry jsflibraryregistry_jsflibraryregistry;




    private jsflibraryregistry_ArchiveFile jsflibraryregistry_archivefile;


    public jsflibraryregistry_JSFLibrary(
        boolean Implementation,        boolean Deployed,        String Name,        String ID,        String JSFVersion    ) {
        this.Implementation = Implementation;
        this.Deployed = Deployed;
        this.Name = Name;
        this.ID = ID;
        this.JSFVersion = JSFVersion;
        this.jsflibraryregistry_archivefiles = new ArrayList<>();
    }

    public jsflibraryregistry_JSFLibrary(
        boolean Implementation,        boolean Deployed,        String Name,        String ID,        String JSFVersion        ArrayList<jsflibraryregistry_ArchiveFile> jsflibraryregistry_archivefiles    ) {
        this.Implementation = Implementation;
        this.Deployed = Deployed;
        this.Name = Name;
        this.ID = ID;
        this.JSFVersion = JSFVersion;
        this.jsflibraryregistry_archivefiles = jsflibraryregistry_archivefiles;
    }

    public boolean getImplementation() {
        return Implementation;
    }

    public void setImplementation(boolean Implementation) {
        this.Implementation = Implementation;
    }
    public boolean getDeployed() {
        return Deployed;
    }

    public void setDeployed(boolean Deployed) {
        this.Deployed = Deployed;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getJsfversion() {
        return JSFVersion;
    }

    public void setJsfversion(String JSFVersion) {
        this.JSFVersion = JSFVersion;
    }

    public List<jsflibraryregistry_ArchiveFile> getJsflibraryregistry_archivefiles() {
        return jsflibraryregistry_archivefiles;
    }

    public void addJsflibraryregistry_archivefile(Jsflibraryregistry_archivefile jsflibraryregistry_archivefile) {
        this.jsflibraryregistry_archivefiles.add(jsflibraryregistry_archivefile);
    }
    public jsflibraryregistry_JSFLibraryRegistry getJsflibraryregistry_jsflibraryregistry() {
        return jsflibraryregistry_jsflibraryregistry;
    }

    public void setJsflibraryregistry_jsflibraryregistry(jsflibraryregistry_JSFLibraryRegistry jsflibraryregistry_jsflibraryregistry) {
        this.jsflibraryregistry_jsflibraryregistry = jsflibraryregistry_jsflibraryregistry;
    }
    public jsflibraryregistry_ArchiveFile getJsflibraryregistry_archivefile() {
        return jsflibraryregistry_archivefile;
    }

    public void setJsflibraryregistry_archivefile(jsflibraryregistry_ArchiveFile jsflibraryregistry_archivefile) {
        this.jsflibraryregistry_archivefile = jsflibraryregistry_archivefile;
    }

}