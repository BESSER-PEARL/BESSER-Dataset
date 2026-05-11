





import java.util.List;
import java.util.ArrayList;

public class simpleClass_ClassModel  {






    private List<simpleClass_Package> simpleclass_packages;


    public simpleClass_ClassModel(
    ) {
        this.simpleclass_packages = new ArrayList<>();
    }

    public simpleClass_ClassModel(
        ArrayList<simpleClass_Package> simpleclass_packages    ) {
        this.simpleclass_packages = simpleclass_packages;
    }


    public List<simpleClass_Package> getSimpleclass_packages() {
        return simpleclass_packages;
    }

    public void addSimpleclass_package(Simpleclass_package simpleclass_package) {
        this.simpleclass_packages.add(simpleclass_package);
    }

}