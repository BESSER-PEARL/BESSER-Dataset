





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractMPackageContainer  {






    private List<jsm_MPackage> jsm_mpackages;




    private jsm_MPackage jsm_mpackage;


    public jsm_AbstractMPackageContainer(
    ) {
        this.jsm_mpackages = new ArrayList<>();
    }

    public jsm_AbstractMPackageContainer(
        ArrayList<jsm_MPackage> jsm_mpackages    ) {
        this.jsm_mpackages = jsm_mpackages;
    }


    public List<jsm_MPackage> getJsm_mpackages() {
        return jsm_mpackages;
    }

    public void addJsm_mpackage(Jsm_mpackage jsm_mpackage) {
        this.jsm_mpackages.add(jsm_mpackage);
    }
    public jsm_MPackage getJsm_mpackage() {
        return jsm_mpackage;
    }

    public void setJsm_mpackage(jsm_MPackage jsm_mpackage) {
        this.jsm_mpackage = jsm_mpackage;
    }

}