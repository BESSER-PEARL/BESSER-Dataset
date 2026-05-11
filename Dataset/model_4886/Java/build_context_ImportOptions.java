





import java.util.List;
import java.util.ArrayList;

public class build_context_ImportOptions  {

    private boolean expand;
    private String suffix;
    private boolean unpack;
    private String resourcePath;
    private String location;
    private String conflictResolution;



    public build_context_ImportOptions(
        boolean expand,        String suffix,        boolean unpack,        String resourcePath,        String location,        String conflictResolution    ) {
        this.expand = expand;
        this.suffix = suffix;
        this.unpack = unpack;
        this.resourcePath = resourcePath;
        this.location = location;
        this.conflictResolution = conflictResolution;
    }


    public boolean getExpand() {
        return expand;
    }

    public void setExpand(boolean expand) {
        this.expand = expand;
    }
    public String getSuffix() {
        return suffix;
    }

    public void setSuffix(String suffix) {
        this.suffix = suffix;
    }
    public boolean getUnpack() {
        return unpack;
    }

    public void setUnpack(boolean unpack) {
        this.unpack = unpack;
    }
    public String getResourcepath() {
        return resourcePath;
    }

    public void setResourcepath(String resourcePath) {
        this.resourcePath = resourcePath;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getConflictresolution() {
        return conflictResolution;
    }

    public void setConflictresolution(String conflictResolution) {
        this.conflictResolution = conflictResolution;
    }


}