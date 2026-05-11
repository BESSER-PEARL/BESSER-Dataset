





import java.util.List;
import java.util.ArrayList;

public class build_context_ResolutionOptions  {

    private boolean filterGroups;
    private String includeParts;
    private String source;
    private boolean prune;
    private String revision;
    private String resolverFilter;
    private String excludeParts;
    private String overlayPath;
    private String mutable;
    private String branchTagPath;
    private String timestamp;



    public build_context_ResolutionOptions(
        boolean filterGroups,        String includeParts,        String source,        boolean prune,        String revision,        String resolverFilter,        String excludeParts,        String overlayPath,        String mutable,        String branchTagPath,        String timestamp    ) {
        this.filterGroups = filterGroups;
        this.includeParts = includeParts;
        this.source = source;
        this.prune = prune;
        this.revision = revision;
        this.resolverFilter = resolverFilter;
        this.excludeParts = excludeParts;
        this.overlayPath = overlayPath;
        this.mutable = mutable;
        this.branchTagPath = branchTagPath;
        this.timestamp = timestamp;
    }


    public boolean getFiltergroups() {
        return filterGroups;
    }

    public void setFiltergroups(boolean filterGroups) {
        this.filterGroups = filterGroups;
    }
    public String getIncludeparts() {
        return includeParts;
    }

    public void setIncludeparts(String includeParts) {
        this.includeParts = includeParts;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public boolean getPrune() {
        return prune;
    }

    public void setPrune(boolean prune) {
        this.prune = prune;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }
    public String getResolverfilter() {
        return resolverFilter;
    }

    public void setResolverfilter(String resolverFilter) {
        this.resolverFilter = resolverFilter;
    }
    public String getExcludeparts() {
        return excludeParts;
    }

    public void setExcludeparts(String excludeParts) {
        this.excludeParts = excludeParts;
    }
    public String getOverlaypath() {
        return overlayPath;
    }

    public void setOverlaypath(String overlayPath) {
        this.overlayPath = overlayPath;
    }
    public String getMutable() {
        return mutable;
    }

    public void setMutable(String mutable) {
        this.mutable = mutable;
    }
    public String getBranchtagpath() {
        return branchTagPath;
    }

    public void setBranchtagpath(String branchTagPath) {
        this.branchTagPath = branchTagPath;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }


}