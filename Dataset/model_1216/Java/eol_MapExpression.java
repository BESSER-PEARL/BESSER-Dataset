





import java.util.List;
import java.util.ArrayList;

public class eol_MapExpression extends LiteralExpression {






    private List<eol_KeyValue> eol_keyvalues;


    public eol_MapExpression(
    ) {
        super(
        );
        this.eol_keyvalues = new ArrayList<>();
    }

    public eol_MapExpression(
        ArrayList<eol_KeyValue> eol_keyvalues    ) {
        this.eol_keyvalues = eol_keyvalues;
    }


    public List<eol_KeyValue> getEol_keyvalues() {
        return eol_keyvalues;
    }

    public void addEol_keyvalue(Eol_keyvalue eol_keyvalue) {
        this.eol_keyvalues.add(eol_keyvalue);
    }

}