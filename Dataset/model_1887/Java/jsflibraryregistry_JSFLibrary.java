





import java.util.List;
import java.util.ArrayList;

public class jsflibraryregistry_JSFLibrary  {

    private String Name;
    private String ID;
    private boolean Implementation;
    private boolean Deployed;
    private String JSFVersion;





    private jsflibraryregistry_JSFLibraryRegistry jsflibraryregistry_jsflibraryregistry;


    public jsflibraryregistry_JSFLibrary(
        String Name,        String ID,        boolean Implementation,        boolean Deployed,        String JSFVersion    ) {
        this.Name = Name;
        this.ID = ID;
        this.Implementation = Implementation;
        this.Deployed = Deployed;
        this.JSFVersion = JSFVersion;
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
    public String getJsfversion() {
        return JSFVersion;
    }

    public void setJsfversion(String JSFVersion) {
        this.JSFVersion = JSFVersion;
    }

    public jsflibraryregistry_JSFLibraryRegistry getJsflibraryregistry_jsflibraryregistry() {
        return jsflibraryregistry_jsflibraryregistry;
    }

    public void setJsflibraryregistry_jsflibraryregistry(jsflibraryregistry_JSFLibraryRegistry jsflibraryregistry_jsflibraryregistry) {
        this.jsflibraryregistry_jsflibraryregistry = jsflibraryregistry_jsflibraryregistry;
    }

}