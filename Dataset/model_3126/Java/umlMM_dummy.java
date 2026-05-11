





import java.util.List;
import java.util.ArrayList;

public class umlMM_dummy  {






    private List<umlMM_Package> umlmm_packages;


    public umlMM_dummy(
    ) {
        this.umlmm_packages = new ArrayList<>();
    }

    public umlMM_dummy(
        ArrayList<umlMM_Package> umlmm_packages    ) {
        this.umlmm_packages = umlmm_packages;
    }


    public List<umlMM_Package> getUmlmm_packages() {
        return umlmm_packages;
    }

    public void addUmlmm_package(Umlmm_package umlmm_package) {
        this.umlmm_packages.add(umlmm_package);
    }

}