





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_SQLSyntaxDefinition  {

    private String terminationCharacter;
    private String operators;
    private String keywords;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_SQLSyntaxDefinition(
        String terminationCharacter,        String operators,        String keywords    ) {
        this.terminationCharacter = terminationCharacter;
        this.operators = operators;
        this.keywords = keywords;
    }


    public String getTerminationcharacter() {
        return terminationCharacter;
    }

    public void setTerminationcharacter(String terminationCharacter) {
        this.terminationCharacter = terminationCharacter;
    }
    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}