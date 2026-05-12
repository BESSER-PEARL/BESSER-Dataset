





import java.util.List;
import java.util.ArrayList;

public class SQLDML_ColumnExp extends NamedElement, Predicate {

    private String alias;



    public SQLDML_ColumnExp(
        String alias    ) {
        super(
        );
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }


}