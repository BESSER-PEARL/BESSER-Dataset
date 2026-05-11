





import java.util.List;
import java.util.ArrayList;

public class build_Branch  {

    private String branchPointType;
    private String acceptDirty;
    private String checkout;
    private String name;
    private String replace;
    private String documentation;
    private String update;
    private String mergeStrategy;





    private List<build_BNamePredicate> build_bnamepredicates;




    private build_Repository build_repository;




    private List<build_BNamePredicate> build_bnamepredicates;




    private build_BExpression build_bexpression;


    public build_Branch(
        String branchPointType,        String acceptDirty,        String checkout,        String name,        String replace,        String documentation,        String update,        String mergeStrategy    ) {
        this.branchPointType = branchPointType;
        this.acceptDirty = acceptDirty;
        this.checkout = checkout;
        this.name = name;
        this.replace = replace;
        this.documentation = documentation;
        this.update = update;
        this.mergeStrategy = mergeStrategy;
        this.build_bnamepredicates = new ArrayList<>();
        this.build_bnamepredicates = new ArrayList<>();
    }

    public build_Branch(
        String branchPointType,        String acceptDirty,        String checkout,        String name,        String replace,        String documentation,        String update,        String mergeStrategy        ArrayList<build_BNamePredicate> build_bnamepredicates,        ArrayList<build_BNamePredicate> build_bnamepredicates    ) {
        this.branchPointType = branchPointType;
        this.acceptDirty = acceptDirty;
        this.checkout = checkout;
        this.name = name;
        this.replace = replace;
        this.documentation = documentation;
        this.update = update;
        this.mergeStrategy = mergeStrategy;
        this.build_bnamepredicates = build_bnamepredicates;
        this.build_bnamepredicates = build_bnamepredicates;
    }

    public String getBranchpointtype() {
        return branchPointType;
    }

    public void setBranchpointtype(String branchPointType) {
        this.branchPointType = branchPointType;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }
    public String getMergestrategy() {
        return mergeStrategy;
    }

    public void setMergestrategy(String mergeStrategy) {
        this.mergeStrategy = mergeStrategy;
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
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }

}