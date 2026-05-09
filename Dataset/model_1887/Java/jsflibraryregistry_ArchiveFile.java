





import java.util.List;
import java.util.ArrayList;

public class jsflibraryregistry_ArchiveFile  {

    private String SourceLocation;
    private boolean RelativeToWorkspace;
    private String RelativeDestLocation;





    private jsflibraryregistry_JSFLibrary jsflibraryregistry_jsflibrary;




    private jsflibraryregistry_JSFLibrary jsflibraryregistry_jsflibrary;


    public jsflibraryregistry_ArchiveFile(
        String SourceLocation,        boolean RelativeToWorkspace,        String RelativeDestLocation    ) {
        this.SourceLocation = SourceLocation;
        this.RelativeToWorkspace = RelativeToWorkspace;
        this.RelativeDestLocation = RelativeDestLocation;
    }


    public String getSourcelocation() {
        return SourceLocation;
    }

    public void setSourcelocation(String SourceLocation) {
        this.SourceLocation = SourceLocation;
    }
    public boolean getRelativetoworkspace() {
        return RelativeToWorkspace;
    }

    public void setRelativetoworkspace(boolean RelativeToWorkspace) {
        this.RelativeToWorkspace = RelativeToWorkspace;
    }
    public String getRelativedestlocation() {
        return RelativeDestLocation;
    }

    public void setRelativedestlocation(String RelativeDestLocation) {
        this.RelativeDestLocation = RelativeDestLocation;
    }

    public jsflibraryregistry_JSFLibrary getJsflibraryregistry_jsflibrary() {
        return jsflibraryregistry_jsflibrary;
    }

    public void setJsflibraryregistry_jsflibrary(jsflibraryregistry_JSFLibrary jsflibraryregistry_jsflibrary) {
        this.jsflibraryregistry_jsflibrary = jsflibraryregistry_jsflibrary;
    }
    public jsflibraryregistry_JSFLibrary getJsflibraryregistry_jsflibrary() {
        return jsflibraryregistry_jsflibrary;
    }

    public void setJsflibraryregistry_jsflibrary(jsflibraryregistry_JSFLibrary jsflibraryregistry_jsflibrary) {
        this.jsflibraryregistry_jsflibrary = jsflibraryregistry_jsflibrary;
    }

}