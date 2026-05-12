





import java.util.List;
import java.util.ArrayList;

public class build_context_ImportOptions  {

    private String suffix;
    private String conflictResolution;
    private String location;
    private boolean expand;
    private String resourcePath;
    private boolean unpack;



    public build_context_ImportOptions(
        String suffix,        String conflictResolution,        String location,        boolean expand,        String resourcePath,        boolean unpack    ) {
        this.suffix = suffix;
        this.conflictResolution = conflictResolution;
        this.location = location;
        this.expand = expand;
        this.resourcePath = resourcePath;
        this.unpack = unpack;
    }


    public String getSuffix() {
        return suffix;
    }

    public void setSuffix(String suffix) {
        this.suffix = suffix;
    }
    public String getConflictresolution() {
        return conflictResolution;
    }

    public void setConflictresolution(String conflictResolution) {
        this.conflictResolution = conflictResolution;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public boolean getExpand() {
        return expand;
    }

    public void setExpand(boolean expand) {
        this.expand = expand;
    }
    public String getResourcepath() {
        return resourcePath;
    }

    public void setResourcepath(String resourcePath) {
        this.resourcePath = resourcePath;
    }
    public boolean getUnpack() {
        return unpack;
    }

    public void setUnpack(boolean unpack) {
        this.unpack = unpack;
    }


}