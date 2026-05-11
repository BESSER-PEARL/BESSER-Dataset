





import java.util.List;
import java.util.ArrayList;

public class Graphql_Attribute  {

    private String isArray;
    private String name;
    private String typeName;
    private String isNullable;





    private Graphql_Type graphql_type;


    public Graphql_Attribute(
        String isArray,        String name,        String typeName,        String isNullable    ) {
        this.isArray = isArray;
        this.name = name;
        this.typeName = typeName;
        this.isNullable = isNullable;
    }


    public String getIsarray() {
        return isArray;
    }

    public void setIsarray(String isArray) {
        this.isArray = isArray;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getIsnullable() {
        return isNullable;
    }

    public void setIsnullable(String isNullable) {
        this.isNullable = isNullable;
    }

    public Graphql_Type getGraphql_type() {
        return graphql_type;
    }

    public void setGraphql_type(Graphql_Type graphql_type) {
        this.graphql_type = graphql_type;
    }

}