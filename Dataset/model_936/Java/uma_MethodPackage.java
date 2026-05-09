





import java.util.List;
import java.util.ArrayList;

public class uma_MethodPackage extends MethodElement {

    private String reusedPackage;
    private String group1;
    private String global_;





    private List<uma_MethodPackage> uma_methodpackages;


    public uma_MethodPackage(
        String reusedPackage,        String group1,        String global_    ) {
        super(
        );
        this.reusedPackage = reusedPackage;
        this.group1 = group1;
        this.global_ = global_;
        this.uma_methodpackages = new ArrayList<>();
    }

    public uma_MethodPackage(
        String reusedPackage,        String group1,        String global_        ArrayList<uma_MethodPackage> uma_methodpackages    ) {
        this.reusedPackage = reusedPackage;
        this.group1 = group1;
        this.global_ = global_;
        this.uma_methodpackages = uma_methodpackages;
    }

    public String getReusedpackage() {
        return reusedPackage;
    }

    public void setReusedpackage(String reusedPackage) {
        this.reusedPackage = reusedPackage;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getGlobal_() {
        return global_;
    }

    public void setGlobal_(String global_) {
        this.global_ = global_;
    }

    public List<uma_MethodPackage> getUma_methodpackages() {
        return uma_methodpackages;
    }

    public void addUma_methodpackage(Uma_methodpackage uma_methodpackage) {
        this.uma_methodpackages.add(uma_methodpackage);
    }

}