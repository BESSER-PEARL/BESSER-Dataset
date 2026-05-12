





import java.util.List;
import java.util.ArrayList;

public class sqls_Enum extends Type {






    private List<sqls_EnumElement> sqls_enumelements;


    public sqls_Enum(
    ) {
        super(
        );
        this.sqls_enumelements = new ArrayList<>();
    }

    public sqls_Enum(
        ArrayList<sqls_EnumElement> sqls_enumelements    ) {
        this.sqls_enumelements = sqls_enumelements;
    }


    public List<sqls_EnumElement> getSqls_enumelements() {
        return sqls_enumelements;
    }

    public void addSqls_enumelement(Sqls_enumelement sqls_enumelement) {
        this.sqls_enumelements.add(sqls_enumelement);
    }

}