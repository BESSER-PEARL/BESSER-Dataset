





import java.util.List;
import java.util.ArrayList;

public class adb_DerivedTypeDefinition extends TypeDefinition {

    private String abstract;
    private String limited;





    private adb_SubtypeIndication adb_subtypeindication;




    private adb_InterfaceList adb_interfacelist;


    public adb_DerivedTypeDefinition(
        String abstract,        String limited    ) {
        super(
        );
        this.abstract = abstract;
        this.limited = limited;
    }


    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getLimited() {
        return limited;
    }

    public void setLimited(String limited) {
        this.limited = limited;
    }

    public adb_SubtypeIndication getAdb_subtypeindication() {
        return adb_subtypeindication;
    }

    public void setAdb_subtypeindication(adb_SubtypeIndication adb_subtypeindication) {
        this.adb_subtypeindication = adb_subtypeindication;
    }
    public adb_InterfaceList getAdb_interfacelist() {
        return adb_interfacelist;
    }

    public void setAdb_interfacelist(adb_InterfaceList adb_interfacelist) {
        this.adb_interfacelist = adb_interfacelist;
    }

}