





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_CreateViewStatement extends DefinitionStatement {

    private String query;
    private String fields;



    public syntax_ddl_CreateViewStatement(
        String query,        String fields    ) {
        super(
        );
        this.query = query;
        this.fields = fields;
    }


    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }
    public String getFields() {
        return fields;
    }

    public void setFields(String fields) {
        this.fields = fields;
    }


}