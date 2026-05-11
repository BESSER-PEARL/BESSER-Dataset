





import java.util.List;
import java.util.ArrayList;

public class adb_FormalPackageDeclaration extends GenericFormalParameterDeclaration {

    private String name;
    private String genericPackageName;



    public adb_FormalPackageDeclaration(
        String name,        String genericPackageName    ) {
        super(
        );
        this.name = name;
        this.genericPackageName = genericPackageName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGenericpackagename() {
        return genericPackageName;
    }

    public void setGenericpackagename(String genericPackageName) {
        this.genericPackageName = genericPackageName;
    }


}