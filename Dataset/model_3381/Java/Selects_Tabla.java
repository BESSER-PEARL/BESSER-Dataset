





import java.util.List;
import java.util.ArrayList;

public class Selects_Tabla extends NamedElement {

    private String tabAlias;



    public Selects_Tabla(
        String tabAlias    ) {
        super(
        );
        this.tabAlias = tabAlias;
    }


    public String getTabalias() {
        return tabAlias;
    }

    public void setTabalias(String tabAlias) {
        this.tabAlias = tabAlias;
    }


}