





import java.util.List;
import java.util.ArrayList;

public class jsflibraryregistry_ArchiveFile  {

    private String RelativeDestLocation;
    private boolean RelativeToWorkspace;
    private String SourceLocation;



    public jsflibraryregistry_ArchiveFile(
        String RelativeDestLocation,        boolean RelativeToWorkspace,        String SourceLocation    ) {
        this.RelativeDestLocation = RelativeDestLocation;
        this.RelativeToWorkspace = RelativeToWorkspace;
        this.SourceLocation = SourceLocation;
    }


    public String getRelativedestlocation() {
        return RelativeDestLocation;
    }

    public void setRelativedestlocation(String RelativeDestLocation) {
        this.RelativeDestLocation = RelativeDestLocation;
    }
    public boolean getRelativetoworkspace() {
        return RelativeToWorkspace;
    }

    public void setRelativetoworkspace(boolean RelativeToWorkspace) {
        this.RelativeToWorkspace = RelativeToWorkspace;
    }
    public String getSourcelocation() {
        return SourceLocation;
    }

    public void setSourcelocation(String SourceLocation) {
        this.SourceLocation = SourceLocation;
    }


}