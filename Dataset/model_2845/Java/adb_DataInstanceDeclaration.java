





import java.util.List;
import java.util.ArrayList;

public class adb_DataInstanceDeclaration extends ObjectDeclaration {

    private boolean constant;
    private boolean aliased;





    private adb_ArrayTypeDefinition adb_arraytypedefinition;




    private adb_AnonymousAccessDefinition adb_anonymousaccessdefinition;




    private adb_SubtypeIndication adb_subtypeindication;




    private adb_Name adb_name;




    private adb_DefiningIdentifierList adb_definingidentifierlist;




    private adb_Expression adb_expression;


    public adb_DataInstanceDeclaration(
        boolean constant,        boolean aliased    ) {
        super(
        );
        this.constant = constant;
        this.aliased = aliased;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public boolean getAliased() {
        return aliased;
    }

    public void setAliased(boolean aliased) {
        this.aliased = aliased;
    }

    public adb_ArrayTypeDefinition getAdb_arraytypedefinition() {
        return adb_arraytypedefinition;
    }

    public void setAdb_arraytypedefinition(adb_ArrayTypeDefinition adb_arraytypedefinition) {
        this.adb_arraytypedefinition = adb_arraytypedefinition;
    }
    public adb_AnonymousAccessDefinition getAdb_anonymousaccessdefinition() {
        return adb_anonymousaccessdefinition;
    }

    public void setAdb_anonymousaccessdefinition(adb_AnonymousAccessDefinition adb_anonymousaccessdefinition) {
        this.adb_anonymousaccessdefinition = adb_anonymousaccessdefinition;
    }
    public adb_SubtypeIndication getAdb_subtypeindication() {
        return adb_subtypeindication;
    }

    public void setAdb_subtypeindication(adb_SubtypeIndication adb_subtypeindication) {
        this.adb_subtypeindication = adb_subtypeindication;
    }
    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }
    public adb_DefiningIdentifierList getAdb_definingidentifierlist() {
        return adb_definingidentifierlist;
    }

    public void setAdb_definingidentifierlist(adb_DefiningIdentifierList adb_definingidentifierlist) {
        this.adb_definingidentifierlist = adb_definingidentifierlist;
    }
    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }

}