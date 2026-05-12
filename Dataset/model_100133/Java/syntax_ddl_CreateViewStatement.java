





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_CreateViewStatement extends DefinitionStatement {

    private String fields;
    private String query;



    public syntax_ddl_CreateViewStatement(
        String fields,        String query    ) {
        super(
        );
        this.fields = fields;
        this.query = query;
    }


    public String getFields() {
        return fields;
    }

    public void setFields(String fields) {
        this.fields = fields;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }


}