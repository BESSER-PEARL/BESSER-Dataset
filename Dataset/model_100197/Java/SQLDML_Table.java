





import java.util.List;
import java.util.ArrayList;

public class SQLDML_Table extends NamedElement {

    private String alias;



    public SQLDML_Table(
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