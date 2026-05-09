





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Package extends Namespace, TemplateableElement, PackageableElement {






    private uml3_0_0_Package uml3_0_0_package;




    private List<uml3_0_0_Package> uml3_0_0_packages;


    public uml3_0_0_Package(
    ) {
        super(
        );
        this.uml3_0_0_packages = new ArrayList<>();
    }

    public uml3_0_0_Package(
        ArrayList<uml3_0_0_Package> uml3_0_0_packages    ) {
        this.uml3_0_0_packages = uml3_0_0_packages;
    }


    public uml3_0_0_Package getUml3_0_0_package() {
        return uml3_0_0_package;
    }

    public void setUml3_0_0_package(uml3_0_0_Package uml3_0_0_package) {
        this.uml3_0_0_package = uml3_0_0_package;
    }
    public List<uml3_0_0_Package> getUml3_0_0_packages() {
        return uml3_0_0_packages;
    }

    public void addUml3_0_0_package(Uml3_0_0_package uml3_0_0_package) {
        this.uml3_0_0_packages.add(uml3_0_0_package);
    }

}