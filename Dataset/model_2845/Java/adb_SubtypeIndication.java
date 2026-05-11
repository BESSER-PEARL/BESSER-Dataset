





import java.util.List;
import java.util.ArrayList;

public class adb_SubtypeIndication extends DiscreteRange, ReturnSubtypeIndication, DiscreteSubtypeDefinition, DiscreteChoice {

    private String subtypeMark;





    private adb_PrivateExtensionDeclaration adb_privateextensiondeclaration;


    public adb_SubtypeIndication(
        String subtypeMark    ) {
        super(
        );
        this.subtypeMark = subtypeMark;
    }


    public String getSubtypemark() {
        return subtypeMark;
    }

    public void setSubtypemark(String subtypeMark) {
        this.subtypeMark = subtypeMark;
    }

    public adb_PrivateExtensionDeclaration getAdb_privateextensiondeclaration() {
        return adb_privateextensiondeclaration;
    }

    public void setAdb_privateextensiondeclaration(adb_PrivateExtensionDeclaration adb_privateextensiondeclaration) {
        this.adb_privateextensiondeclaration = adb_privateextensiondeclaration;
    }

}