





import java.util.List;
import java.util.ArrayList;

public class relationaldatabase_Tag  {

    private String name;
    private String documentation;





    private relationaldatabase_DatabaseModel relationaldatabase_databasemodel;


    public relationaldatabase_Tag(
        String name,        String documentation    ) {
        this.name = name;
        this.documentation = documentation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }

    public relationaldatabase_DatabaseModel getRelationaldatabase_databasemodel() {
        return relationaldatabase_databasemodel;
    }

    public void setRelationaldatabase_databasemodel(relationaldatabase_DatabaseModel relationaldatabase_databasemodel) {
        this.relationaldatabase_databasemodel = relationaldatabase_databasemodel;
    }

}