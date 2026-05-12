





import java.util.List;
import java.util.ArrayList;

public class build_context_ResolutionOptions  {

    private boolean filterGroups;
    private String branchTagPath;
    private String revision;
    private String includeParts;
    private String mutable;
    private String overlayPath;
    private String timestamp;
    private String resolverFilter;
    private String excludeParts;
    private String source;
    private boolean prune;



    public build_context_ResolutionOptions(
        boolean filterGroups,        String branchTagPath,        String revision,        String includeParts,        String mutable,        String overlayPath,        String timestamp,        String resolverFilter,        String excludeParts,        String source,        boolean prune    ) {
        this.filterGroups = filterGroups;
        this.branchTagPath = branchTagPath;
        this.revision = revision;
        this.includeParts = includeParts;
        this.mutable = mutable;
        this.overlayPath = overlayPath;
        this.timestamp = timestamp;
        this.resolverFilter = resolverFilter;
        this.excludeParts = excludeParts;
        this.source = source;
        this.prune = prune;
    }


    public boolean getFiltergroups() {
        return filterGroups;
    }

    public void setFiltergroups(boolean filterGroups) {
        this.filterGroups = filterGroups;
    }
    public String getBranchtagpath() {
        return branchTagPath;
    }

    public void setBranchtagpath(String branchTagPath) {
        this.branchTagPath = branchTagPath;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }
    public String getIncludeparts() {
        return includeParts;
    }

    public void setIncludeparts(String includeParts) {
        this.includeParts = includeParts;
    }
    public String getMutable() {
        return mutable;
    }

    public void setMutable(String mutable) {
        this.mutable = mutable;
    }
    public String getOverlaypath() {
        return overlayPath;
    }

    public void setOverlaypath(String overlayPath) {
        this.overlayPath = overlayPath;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
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


}