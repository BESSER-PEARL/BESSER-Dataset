





import java.util.List;
import java.util.ArrayList;

public class emig_OpDef extends LocatedElement {

    private String op;





    private List<emig_setterDef> emig_setterdefs;




    private emig_Rule emig_rule;


    public emig_OpDef(
        String op    ) {
        super(
        );
        this.op = op;
        this.emig_setterdefs = new ArrayList<>();
    }

    public emig_OpDef(
        String op        ArrayList<emig_setterDef> emig_setterdefs    ) {
        this.op = op;
        this.emig_setterdefs = emig_setterdefs;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<emig_setterDef> getEmig_setterdefs() {
        return emig_setterdefs;
    }

    public void addEmig_setterdef(Emig_setterdef emig_setterdef) {
        this.emig_setterdefs.add(emig_setterdef);
    }
    public emig_Rule getEmig_rule() {
        return emig_rule;
    }

    public void setEmig_rule(emig_Rule emig_rule) {
        this.emig_rule = emig_rule;
    }

}