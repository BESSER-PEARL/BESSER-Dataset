





import java.util.List;
import java.util.ArrayList;

public class uma_MethodPackage extends MethodElement, Package {

    private String global_;





    private uma_MethodConfiguration uma_methodconfiguration;




    private List<uma_MethodPackage> uma_methodpackages;




    private uma_MethodPackage uma_methodpackage;




    private uma_MethodPackage uma_methodpackage;


    public uma_MethodPackage(
        String global_    ) {
        super(
        );
        this.global_ = global_;
        this.uma_methodpackages = new ArrayList<>();
    }

    public uma_MethodPackage(
        String global_        ArrayList<uma_MethodPackage> uma_methodpackages    ) {
        this.global_ = global_;
        this.uma_methodpackages = uma_methodpackages;
    }

    public String getGlobal_() {
        return global_;
    }

    public void setGlobal_(String global_) {
        this.global_ = global_;
    }

    public uma_MethodConfiguration getUma_methodconfiguration() {
        return uma_methodconfiguration;
    }

    public void setUma_methodconfiguration(uma_MethodConfiguration uma_methodconfiguration) {
        this.uma_methodconfiguration = uma_methodconfiguration;
    }
    public List<uma_MethodPackage> getUma_methodpackages() {
        return uma_methodpackages;
    }

    public void addUma_methodpackage(Uma_methodpackage uma_methodpackage) {
        this.uma_methodpackages.add(uma_methodpackage);
    }
    public uma_MethodPackage getUma_methodpackage() {
        return uma_methodpackage;
    }

    public void setUma_methodpackage(uma_MethodPackage uma_methodpackage) {
        this.uma_methodpackage = uma_methodpackage;
    }
    public uma_MethodPackage getUma_methodpackage() {
        return uma_methodpackage;
    }

    public void setUma_methodpackage(uma_MethodPackage uma_methodpackage) {
        this.uma_methodpackage = uma_methodpackage;
    }

}