





import java.util.List;
import java.util.ArrayList;

public class yyk_Relation extends NamedElement {

    private String since;





    private yyk_Rel yyk_rel;




    private yyk_Base yyk_base;




    private yyk_Base yyk_base;




    private yyk_Relation yyk_relation;


    public yyk_Relation(
        String since    ) {
        super(
        );
        this.since = since;
    }


    public String getSince() {
        return since;
    }

    public void setSince(String since) {
        this.since = since;
    }

    public yyk_Rel getYyk_rel() {
        return yyk_rel;
    }

    public void setYyk_rel(yyk_Rel yyk_rel) {
        this.yyk_rel = yyk_rel;
    }
    public yyk_Base getYyk_base() {
        return yyk_base;
    }

    public void setYyk_base(yyk_Base yyk_base) {
        this.yyk_base = yyk_base;
    }
    public yyk_Base getYyk_base() {
        return yyk_base;
    }

    public void setYyk_base(yyk_Base yyk_base) {
        this.yyk_base = yyk_base;
    }
    public yyk_Relation getYyk_relation() {
        return yyk_relation;
    }

    public void setYyk_relation(yyk_Relation yyk_relation) {
        this.yyk_relation = yyk_relation;
    }

}