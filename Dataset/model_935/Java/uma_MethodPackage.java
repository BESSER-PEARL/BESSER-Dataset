





import java.util.List;
import java.util.ArrayList;

public class uma_MethodPackage extends MethodElement {

    private String reusedPackage;
    private String global_;
    private String group1;





    private uma_MethodPackage uma_methodpackage;


    public uma_MethodPackage(
        String reusedPackage,        String global_,        String group1    ) {
        super(
        );
        this.reusedPackage = reusedPackage;
        this.global_ = global_;
        this.group1 = group1;
    }


    public String getReusedpackage() {
        return reusedPackage;
    }

    public void setReusedpackage(String reusedPackage) {
        this.reusedPackage = reusedPackage;
    }
    public String getGlobal_() {
        return global_;
    }

    public void setGlobal_(String global_) {
        this.global_ = global_;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }

    public uma_MethodPackage getUma_methodpackage() {
        return uma_methodpackage;
    }

    public void setUma_methodpackage(uma_MethodPackage uma_methodpackage) {
        this.uma_methodpackage = uma_methodpackage;
    }

}