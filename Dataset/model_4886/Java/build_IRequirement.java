





import java.util.List;
import java.util.ArrayList;

public class build_IRequirement  {

    private String filter;
    private String alias;
    private String excludePattern;
    private boolean contributor;
    private String memberName;
    private String includePattern;





    private build_IPrerequisites build_iprerequisites;


    public build_IRequirement(
        String filter,        String alias,        String excludePattern,        boolean contributor,        String memberName,        String includePattern    ) {
        this.filter = filter;
        this.alias = alias;
        this.excludePattern = excludePattern;
        this.contributor = contributor;
        this.memberName = memberName;
        this.includePattern = includePattern;
    }


    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getExcludepattern() {
        return excludePattern;
    }

    public void setExcludepattern(String excludePattern) {
        this.excludePattern = excludePattern;
    }
    public boolean getContributor() {
        return contributor;
    }

    public void setContributor(boolean contributor) {
        this.contributor = contributor;
    }
    public String getMembername() {
        return memberName;
    }

    public void setMembername(String memberName) {
        this.memberName = memberName;
    }
    public String getIncludepattern() {
        return includePattern;
    }

    public void setIncludepattern(String includePattern) {
        this.includePattern = includePattern;
    }

    public build_IPrerequisites getBuild_iprerequisites() {
        return build_iprerequisites;
    }

    public void setBuild_iprerequisites(build_IPrerequisites build_iprerequisites) {
        this.build_iprerequisites = build_iprerequisites;
    }

}