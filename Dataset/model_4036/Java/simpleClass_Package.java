





import java.util.List;
import java.util.ArrayList;

public class simpleClass_Package extends NamedElement {






    private List<simpleClass_Association> simpleclass_associations;




    private List<simpleClass_Package> simpleclass_packages;




    private List<simpleClass_Class> simpleclass_classs;


    public simpleClass_Package(
    ) {
        super(
        );
        this.simpleclass_associations = new ArrayList<>();
        this.simpleclass_packages = new ArrayList<>();
        this.simpleclass_classs = new ArrayList<>();
    }

    public simpleClass_Package(
        ArrayList<simpleClass_Association> simpleclass_associations,        ArrayList<simpleClass_Package> simpleclass_packages,        ArrayList<simpleClass_Class> simpleclass_classs    ) {
        this.simpleclass_associations = simpleclass_associations;
        this.simpleclass_packages = simpleclass_packages;
        this.simpleclass_classs = simpleclass_classs;
    }


    public List<simpleClass_Association> getSimpleclass_associations() {
        return simpleclass_associations;
    }

    public void addSimpleclass_association(Simpleclass_association simpleclass_association) {
        this.simpleclass_associations.add(simpleclass_association);
    }
    public List<simpleClass_Package> getSimpleclass_packages() {
        return simpleclass_packages;
    }

    public void addSimpleclass_package(Simpleclass_package simpleclass_package) {
        this.simpleclass_packages.add(simpleclass_package);
    }
    public List<simpleClass_Class> getSimpleclass_classs() {
        return simpleclass_classs;
    }

    public void addSimpleclass_class(Simpleclass_class simpleclass_class) {
        this.simpleclass_classs.add(simpleclass_class);
    }

}