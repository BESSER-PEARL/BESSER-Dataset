





import java.util.List;
import java.util.ArrayList;

public class types_Package extends NamedElement {






    private types_Package types_package;




    private List<types_PackageMember> types_packagemembers;


    public types_Package(
    ) {
        super(
        );
        this.types_packagemembers = new ArrayList<>();
    }

    public types_Package(
        ArrayList<types_PackageMember> types_packagemembers    ) {
        this.types_packagemembers = types_packagemembers;
    }


    public types_Package getTypes_package() {
        return types_package;
    }

    public void setTypes_package(types_Package types_package) {
        this.types_package = types_package;
    }
    public List<types_PackageMember> getTypes_packagemembers() {
        return types_packagemembers;
    }

    public void addTypes_packagemember(Types_packagemember types_packagemember) {
        this.types_packagemembers.add(types_packagemember);
    }

}