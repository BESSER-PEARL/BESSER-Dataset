





import java.util.List;
import java.util.ArrayList;

public class build_Branch  {

    private String acceptDirty;
    private String checkout;
    private String mergeStrategy;
    private String update;
    private String branchPointType;
    private String replace;
    private String documentation;
    private String name;





    private List<build_BNamePredicate> build_bnamepredicates;




    private build_Repository build_repository;




    private List<build_BNamePredicate> build_bnamepredicates;


    public build_Branch(
        String acceptDirty,        String checkout,        String mergeStrategy,        String update,        String branchPointType,        String replace,        String documentation,        String name    ) {
        this.acceptDirty = acceptDirty;
        this.checkout = checkout;
        this.mergeStrategy = mergeStrategy;
        this.update = update;
        this.branchPointType = branchPointType;
        this.replace = replace;
        this.documentation = documentation;
        this.name = name;
        this.build_bnamepredicates = new ArrayList<>();
        this.build_bnamepredicates = new ArrayList<>();
    }

    public build_Branch(
        String acceptDirty,        String checkout,        String mergeStrategy,        String update,        String branchPointType,        String replace,        String documentation,        String name        ArrayList<build_BNamePredicate> build_bnamepredicates,        ArrayList<build_BNamePredicate> build_bnamepredicates    ) {
        this.acceptDirty = acceptDirty;
        this.checkout = checkout;
        this.mergeStrategy = mergeStrategy;
        this.update = update;
        this.branchPointType = branchPointType;
        this.replace = replace;
        this.documentation = documentation;
        this.name = name;
        this.build_bnamepredicates = build_bnamepredicates;
        this.build_bnamepredicates = build_bnamepredicates;
    }

    public String getAcceptdirty() {
        return acceptDirty;
    }

    public void setAcceptdirty(String acceptDirty) {
        this.acceptDirty = acceptDirty;
    }
    public String getCheckout() {
        return checkout;
    }

    public void setCheckout(String checkout) {
        this.checkout = checkout;
    }
    public String getMergestrategy() {
        return mergeStrategy;
    }

    public void setMergestrategy(String mergeStrategy) {
        this.mergeStrategy = mergeStrategy;
    }
    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }
    public String getBranchpointtype() {
        return branchPointType;
    }

    public void setBranchpointtype(String branchPointType) {
        this.branchPointType = branchPointType;
    }
    public String getReplace() {
        return replace;
    }

    public void setReplace(String replace) {
        this.replace = replace;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<build_BNamePredicate> getBuild_bnamepredicates() {
        return build_bnamepredicates;
    }

    public void addBuild_bnamepredicate(Build_bnamepredicate build_bnamepredicate) {
        this.build_bnamepredicates.add(build_bnamepredicate);
    }
    public build_Repository getBuild_repository() {
        return build_repository;
    }

    public void setBuild_repository(build_Repository build_repository) {
        this.build_repository = build_repository;
    }
    public List<build_BNamePredicate> getBuild_bnamepredicates() {
        return build_bnamepredicates;
    }

    public void addBuild_bnamepredicate(Build_bnamepredicate build_bnamepredicate) {
        this.build_bnamepredicates.add(build_bnamepredicate);
    }

}