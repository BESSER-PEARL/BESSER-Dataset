





import java.util.List;
import java.util.ArrayList;

public class adb_FormalTypeDeclaration extends GenericFormalParameterDeclaration {

    private String identifier;





    private adb_DiscriminantPart adb_discriminantpart;




    private adb_FormalTypeDefinition adb_formaltypedefinition;


    public adb_FormalTypeDeclaration(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public adb_DiscriminantPart getAdb_discriminantpart() {
        return adb_discriminantpart;
    }

    public void setAdb_discriminantpart(adb_DiscriminantPart adb_discriminantpart) {
        this.adb_discriminantpart = adb_discriminantpart;
    }
    public adb_FormalTypeDefinition getAdb_formaltypedefinition() {
        return adb_formaltypedefinition;
    }

    public void setAdb_formaltypedefinition(adb_FormalTypeDefinition adb_formaltypedefinition) {
        this.adb_formaltypedefinition = adb_formaltypedefinition;
    }

}