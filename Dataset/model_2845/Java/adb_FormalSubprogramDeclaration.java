





import java.util.List;
import java.util.ArrayList;

public class adb_FormalSubprogramDeclaration extends GenericFormalParameterDeclaration {

    private String abstract;





    private adb_SubprogramSpecification adb_subprogramspecification;


    public adb_FormalSubprogramDeclaration(
        String abstract    ) {
        super(
        );
        this.abstract = abstract;
    }


    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }

    public adb_SubprogramSpecification getAdb_subprogramspecification() {
        return adb_subprogramspecification;
    }

    public void setAdb_subprogramspecification(adb_SubprogramSpecification adb_subprogramspecification) {
        this.adb_subprogramspecification = adb_subprogramspecification;
    }

}