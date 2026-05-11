





import java.util.List;
import java.util.ArrayList;

public class adb_SubprogramSpecification extends LibrarySpecification, LibraryUnitSpecification, BodyStub {






    private adb_SubprogramDeclaration adb_subprogramdeclaration;




    private adb_OverridingIndicator adb_overridingindicator;




    private adb_SubprogramBody adb_subprogrambody;


    public adb_SubprogramSpecification(
    ) {
        super(
        );
    }



    public adb_SubprogramDeclaration getAdb_subprogramdeclaration() {
        return adb_subprogramdeclaration;
    }

    public void setAdb_subprogramdeclaration(adb_SubprogramDeclaration adb_subprogramdeclaration) {
        this.adb_subprogramdeclaration = adb_subprogramdeclaration;
    }
    public adb_OverridingIndicator getAdb_overridingindicator() {
        return adb_overridingindicator;
    }

    public void setAdb_overridingindicator(adb_OverridingIndicator adb_overridingindicator) {
        this.adb_overridingindicator = adb_overridingindicator;
    }
    public adb_SubprogramBody getAdb_subprogrambody() {
        return adb_subprogrambody;
    }

    public void setAdb_subprogrambody(adb_SubprogramBody adb_subprogrambody) {
        this.adb_subprogrambody = adb_subprogrambody;
    }

}