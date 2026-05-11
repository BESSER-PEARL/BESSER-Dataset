





import java.util.List;
import java.util.ArrayList;

public class adb_GenericInstantiation extends LibraryUnitSpecification, BasicDeclaration {

    private String name;
    private String genericName;



    public adb_GenericInstantiation(
        String name,        String genericName    ) {
        super(
        );
        this.name = name;
        this.genericName = genericName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGenericname() {
        return genericName;
    }

    public void setGenericname(String genericName) {
        this.genericName = genericName;
    }


}