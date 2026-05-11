





import java.util.List;
import java.util.ArrayList;

public class simpleClass_Package extends NamedElement {






    private List<simpleClass_Package> simpleclass_packages;




    private simpleClass_ClassModel simpleclass_classmodel;


    public simpleClass_Package(
    ) {
        super(
        );
        this.simpleclass_packages = new ArrayList<>();
    }

    public simpleClass_Package(
        ArrayList<simpleClass_Package> simpleclass_packages    ) {
        this.simpleclass_packages = simpleclass_packages;
    }


    public List<simpleClass_Package> getSimpleclass_packages() {
        return simpleclass_packages;
    }

    public void addSimpleclass_package(Simpleclass_package simpleclass_package) {
        this.simpleclass_packages.add(simpleclass_package);
    }
    public simpleClass_ClassModel getSimpleclass_classmodel() {
        return simpleclass_classmodel;
    }

    public void setSimpleclass_classmodel(simpleClass_ClassModel simpleclass_classmodel) {
        this.simpleclass_classmodel = simpleclass_classmodel;
    }

}