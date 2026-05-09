





import java.util.List;
import java.util.ArrayList;

public class yyk_NamedElement  {

    private String name;





    private yyk_Rel yyk_rel;




    private List<yyk_Bar> yyk_bars;




    private yyk_Relation yyk_relation;




    private List<yyk_Alias> yyk_aliass;




    private List<yyk_Rel> yyk_rels;


    public yyk_NamedElement(
        String name    ) {
        this.name = name;
        this.yyk_bars = new ArrayList<>();
        this.yyk_aliass = new ArrayList<>();
        this.yyk_rels = new ArrayList<>();
    }

    public yyk_NamedElement(
        String name        ArrayList<yyk_Bar> yyk_bars,        ArrayList<yyk_Alias> yyk_aliass,        ArrayList<yyk_Rel> yyk_rels    ) {
        this.name = name;
        this.yyk_bars = yyk_bars;
        this.yyk_aliass = yyk_aliass;
        this.yyk_rels = yyk_rels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public yyk_Rel getYyk_rel() {
        return yyk_rel;
    }

    public void setYyk_rel(yyk_Rel yyk_rel) {
        this.yyk_rel = yyk_rel;
    }
    public List<yyk_Bar> getYyk_bars() {
        return yyk_bars;
    }

    public void addYyk_bar(Yyk_bar yyk_bar) {
        this.yyk_bars.add(yyk_bar);
    }
    public yyk_Relation getYyk_relation() {
        return yyk_relation;
    }

    public void setYyk_relation(yyk_Relation yyk_relation) {
        this.yyk_relation = yyk_relation;
    }
    public List<yyk_Alias> getYyk_aliass() {
        return yyk_aliass;
    }

    public void addYyk_alias(Yyk_alias yyk_alias) {
        this.yyk_aliass.add(yyk_alias);
    }
    public List<yyk_Rel> getYyk_rels() {
        return yyk_rels;
    }

    public void addYyk_rel(Yyk_rel yyk_rel) {
        this.yyk_rels.add(yyk_rel);
    }

}