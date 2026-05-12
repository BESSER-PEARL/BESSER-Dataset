





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_PrivilegedElementDefinition  {

    private String name;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_PrivilegedElementDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}