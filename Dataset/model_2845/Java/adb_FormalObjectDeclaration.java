





import java.util.List;
import java.util.ArrayList;

public class adb_FormalObjectDeclaration extends GenericFormalParameterDeclaration {






    private adb_Expression adb_expression;




    private adb_AnonymousAccessDefinition adb_anonymousaccessdefinition;




    private adb_Name adb_name;


    public adb_FormalObjectDeclaration(
    ) {
        super(
        );
    }



    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }
    public adb_AnonymousAccessDefinition getAdb_anonymousaccessdefinition() {
        return adb_anonymousaccessdefinition;
    }

    public void setAdb_anonymousaccessdefinition(adb_AnonymousAccessDefinition adb_anonymousaccessdefinition) {
        this.adb_anonymousaccessdefinition = adb_anonymousaccessdefinition;
    }
    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }

}