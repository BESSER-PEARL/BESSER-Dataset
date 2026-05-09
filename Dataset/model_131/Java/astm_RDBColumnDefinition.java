





import java.util.List;
import java.util.ArrayList;

public class astm_RDBColumnDefinition extends Definition {

    private boolean NotNull;





    private astm_RDBTableDefinition astm_rdbtabledefinition;




    private astm_Name astm_name;


    public astm_RDBColumnDefinition(
        boolean NotNull    ) {
        super(
        );
        this.NotNull = NotNull;
    }


    public boolean getNotnull() {
        return NotNull;
    }

    public void setNotnull(boolean NotNull) {
        this.NotNull = NotNull;
    }

    public astm_RDBTableDefinition getAstm_rdbtabledefinition() {
        return astm_rdbtabledefinition;
    }

    public void setAstm_rdbtabledefinition(astm_RDBTableDefinition astm_rdbtabledefinition) {
        this.astm_rdbtabledefinition = astm_rdbtabledefinition;
    }
    public astm_Name getAstm_name() {
        return astm_name;
    }

    public void setAstm_name(astm_Name astm_name) {
        this.astm_name = astm_name;
    }

}