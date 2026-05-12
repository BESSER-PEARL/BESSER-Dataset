





import java.util.List;
import java.util.ArrayList;

public class unql_Select  {

    private String attributes;
    private String conditions;
    private String relations;





    private unql_Program unql_program;


    public unql_Select(
        String attributes,        String conditions,        String relations    ) {
        this.attributes = attributes;
        this.conditions = conditions;
        this.relations = relations;
    }


    public String getAttributes() {
        return attributes;
    }

    public void setAttributes(String attributes) {
        this.attributes = attributes;
    }
    public String getConditions() {
        return conditions;
    }

    public void setConditions(String conditions) {
        this.conditions = conditions;
    }
    public String getRelations() {
        return relations;
    }

    public void setRelations(String relations) {
        this.relations = relations;
    }

    public unql_Program getUnql_program() {
        return unql_program;
    }

    public void setUnql_program(unql_Program unql_program) {
        this.unql_program = unql_program;
    }

}