





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_PrivilegeDefinition  {

    private String name;





    private dbdefinition_PrivilegedElementDefinition dbdefinition_privilegedelementdefinition;




    private List<dbdefinition_PrivilegedElementDefinition> dbdefinition_privilegedelementdefinitions;


    public dbdefinition_PrivilegeDefinition(
        String name    ) {
        this.name = name;
        this.dbdefinition_privilegedelementdefinitions = new ArrayList<>();
    }

    public dbdefinition_PrivilegeDefinition(
        String name        ArrayList<dbdefinition_PrivilegedElementDefinition> dbdefinition_privilegedelementdefinitions    ) {
        this.name = name;
        this.dbdefinition_privilegedelementdefinitions = dbdefinition_privilegedelementdefinitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbdefinition_PrivilegedElementDefinition getDbdefinition_privilegedelementdefinition() {
        return dbdefinition_privilegedelementdefinition;
    }

    public void setDbdefinition_privilegedelementdefinition(dbdefinition_PrivilegedElementDefinition dbdefinition_privilegedelementdefinition) {
        this.dbdefinition_privilegedelementdefinition = dbdefinition_privilegedelementdefinition;
    }
    public List<dbdefinition_PrivilegedElementDefinition> getDbdefinition_privilegedelementdefinitions() {
        return dbdefinition_privilegedelementdefinitions;
    }

    public void addDbdefinition_privilegedelementdefinition(Dbdefinition_privilegedelementdefinition dbdefinition_privilegedelementdefinition) {
        this.dbdefinition_privilegedelementdefinitions.add(dbdefinition_privilegedelementdefinition);
    }

}