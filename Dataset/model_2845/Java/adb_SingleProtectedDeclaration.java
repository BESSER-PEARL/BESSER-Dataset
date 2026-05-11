





import java.util.List;
import java.util.ArrayList;

public class adb_SingleProtectedDeclaration extends ObjectDeclaration {

    private String name;





    private adb_ProtectedDefinition adb_protecteddefinition;




    private adb_InterfaceList adb_interfacelist;


    public adb_SingleProtectedDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adb_ProtectedDefinition getAdb_protecteddefinition() {
        return adb_protecteddefinition;
    }

    public void setAdb_protecteddefinition(adb_ProtectedDefinition adb_protecteddefinition) {
        this.adb_protecteddefinition = adb_protecteddefinition;
    }
    public adb_InterfaceList getAdb_interfacelist() {
        return adb_interfacelist;
    }

    public void setAdb_interfacelist(adb_InterfaceList adb_interfacelist) {
        this.adb_interfacelist = adb_interfacelist;
    }

}