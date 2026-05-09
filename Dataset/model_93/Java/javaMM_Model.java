





import java.util.List;
import java.util.ArrayList;

public class javaMM_Model  {

    private String name;





    private javaMM_Package javamm_package;




    private List<javaMM_Package> javamm_packages;


    public javaMM_Model(
        String name    ) {
        this.name = name;
        this.javamm_packages = new ArrayList<>();
    }

    public javaMM_Model(
        String name        ArrayList<javaMM_Package> javamm_packages    ) {
        this.name = name;
        this.javamm_packages = javamm_packages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }
    public List<javaMM_Package> getJavamm_packages() {
        return javamm_packages;
    }

    public void addJavamm_package(Javamm_package javamm_package) {
        this.javamm_packages.add(javamm_package);
    }

}