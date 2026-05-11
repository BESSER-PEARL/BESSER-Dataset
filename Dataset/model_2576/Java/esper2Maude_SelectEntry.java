





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_SelectEntry  {

    private String groupOp;
    private String alias;





    private esper2Maude_LastSelectEntry esper2maude_lastselectentry;




    private esper2Maude_Field esper2maude_field;




    private esper2Maude_NonLastSelectEntry esper2maude_nonlastselectentry;


    public esper2Maude_SelectEntry(
        String groupOp,        String alias    ) {
        this.groupOp = groupOp;
        this.alias = alias;
    }


    public String getGroupop() {
        return groupOp;
    }

    public void setGroupop(String groupOp) {
        this.groupOp = groupOp;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public esper2Maude_LastSelectEntry getEsper2maude_lastselectentry() {
        return esper2maude_lastselectentry;
    }

    public void setEsper2maude_lastselectentry(esper2Maude_LastSelectEntry esper2maude_lastselectentry) {
        this.esper2maude_lastselectentry = esper2maude_lastselectentry;
    }
    public esper2Maude_Field getEsper2maude_field() {
        return esper2maude_field;
    }

    public void setEsper2maude_field(esper2Maude_Field esper2maude_field) {
        this.esper2maude_field = esper2maude_field;
    }
    public esper2Maude_NonLastSelectEntry getEsper2maude_nonlastselectentry() {
        return esper2maude_nonlastselectentry;
    }

    public void setEsper2maude_nonlastselectentry(esper2Maude_NonLastSelectEntry esper2maude_nonlastselectentry) {
        this.esper2maude_nonlastselectentry = esper2maude_nonlastselectentry;
    }

}