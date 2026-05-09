





import java.util.List;
import java.util.ArrayList;

public class astm_AggregateTypeDefinition extends TypeDefinition {






    private astm_RDBViewDefinition astm_rdbviewdefinition;




    private astm_RDBCursorDefinition astm_rdbcursordefinition;


    public astm_AggregateTypeDefinition(
    ) {
        super(
        );
    }



    public astm_RDBViewDefinition getAstm_rdbviewdefinition() {
        return astm_rdbviewdefinition;
    }

    public void setAstm_rdbviewdefinition(astm_RDBViewDefinition astm_rdbviewdefinition) {
        this.astm_rdbviewdefinition = astm_rdbviewdefinition;
    }
    public astm_RDBCursorDefinition getAstm_rdbcursordefinition() {
        return astm_rdbcursordefinition;
    }

    public void setAstm_rdbcursordefinition(astm_RDBCursorDefinition astm_rdbcursordefinition) {
        this.astm_rdbcursordefinition = astm_rdbcursordefinition;
    }

}