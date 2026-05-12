





import java.util.List;
import java.util.ArrayList;

public class Relational_EnumeratedLiteral  {

    private String name;





    private Relational_EnumerationType relational_enumerationtype;


    public Relational_EnumeratedLiteral(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Relational_EnumerationType getRelational_enumerationtype() {
        return relational_enumerationtype;
    }

    public void setRelational_enumerationtype(Relational_EnumerationType relational_enumerationtype) {
        this.relational_enumerationtype = relational_enumerationtype;
    }

}