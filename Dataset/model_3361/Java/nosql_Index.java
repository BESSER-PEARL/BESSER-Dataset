





import java.util.List;
import java.util.ArrayList;

public class nosql_Index  {

    private String reference;
    private String name;





    private nosql_KeySpace nosql_keyspace;


    public nosql_Index(
        String reference,        String name    ) {
        this.reference = reference;
        this.name = name;
    }


    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nosql_KeySpace getNosql_keyspace() {
        return nosql_keyspace;
    }

    public void setNosql_keyspace(nosql_KeySpace nosql_keyspace) {
        this.nosql_keyspace = nosql_keyspace;
    }

}