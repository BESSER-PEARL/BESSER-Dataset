





import java.util.List;
import java.util.ArrayList;

public class yye_Relation extends NamedElement {

    private String since;





    private List<yye_Relation> yye_relations;




    private yye_Base yye_base;




    private yye_Base yye_base;




    private yye_Base yye_base;


    public yye_Relation(
        String since    ) {
        super(
        );
        this.since = since;
        this.yye_relations = new ArrayList<>();
    }

    public yye_Relation(
        String since        ArrayList<yye_Relation> yye_relations    ) {
        this.since = since;
        this.yye_relations = yye_relations;
    }

    public String getSince() {
        return since;
    }

    public void setSince(String since) {
        this.since = since;
    }

    public List<yye_Relation> getYye_relations() {
        return yye_relations;
    }

    public void addYye_relation(Yye_relation yye_relation) {
        this.yye_relations.add(yye_relation);
    }
    public yye_Base getYye_base() {
        return yye_base;
    }

    public void setYye_base(yye_Base yye_base) {
        this.yye_base = yye_base;
    }
    public yye_Base getYye_base() {
        return yye_base;
    }

    public void setYye_base(yye_Base yye_base) {
        this.yye_base = yye_base;
    }
    public yye_Base getYye_base() {
        return yye_base;
    }

    public void setYye_base(yye_Base yye_base) {
        this.yye_base = yye_base;
    }

}