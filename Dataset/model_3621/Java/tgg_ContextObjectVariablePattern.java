





import java.util.List;
import java.util.ArrayList;

public class tgg_ContextObjectVariablePattern  {

    private String name;





    private List<tgg_ContextLinkVariablePattern> tgg_contextlinkvariablepatterns;




    private List<tgg_AttributeConstraint> tgg_attributeconstraints;




    private tgg_Nac tgg_nac;




    private tgg_Nac tgg_nac;




    private tgg_EClass tgg_eclass;




    private tgg_ContextLinkVariablePattern tgg_contextlinkvariablepattern;


    public tgg_ContextObjectVariablePattern(
        String name    ) {
        this.name = name;
        this.tgg_contextlinkvariablepatterns = new ArrayList<>();
        this.tgg_attributeconstraints = new ArrayList<>();
    }

    public tgg_ContextObjectVariablePattern(
        String name        ArrayList<tgg_ContextLinkVariablePattern> tgg_contextlinkvariablepatterns,        ArrayList<tgg_AttributeConstraint> tgg_attributeconstraints    ) {
        this.name = name;
        this.tgg_contextlinkvariablepatterns = tgg_contextlinkvariablepatterns;
        this.tgg_attributeconstraints = tgg_attributeconstraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tgg_ContextLinkVariablePattern> getTgg_contextlinkvariablepatterns() {
        return tgg_contextlinkvariablepatterns;
    }

    public void addTgg_contextlinkvariablepattern(Tgg_contextlinkvariablepattern tgg_contextlinkvariablepattern) {
        this.tgg_contextlinkvariablepatterns.add(tgg_contextlinkvariablepattern);
    }
    public List<tgg_AttributeConstraint> getTgg_attributeconstraints() {
        return tgg_attributeconstraints;
    }

    public void addTgg_attributeconstraint(Tgg_attributeconstraint tgg_attributeconstraint) {
        this.tgg_attributeconstraints.add(tgg_attributeconstraint);
    }
    public tgg_Nac getTgg_nac() {
        return tgg_nac;
    }

    public void setTgg_nac(tgg_Nac tgg_nac) {
        this.tgg_nac = tgg_nac;
    }
    public tgg_Nac getTgg_nac() {
        return tgg_nac;
    }

    public void setTgg_nac(tgg_Nac tgg_nac) {
        this.tgg_nac = tgg_nac;
    }
    public tgg_EClass getTgg_eclass() {
        return tgg_eclass;
    }

    public void setTgg_eclass(tgg_EClass tgg_eclass) {
        this.tgg_eclass = tgg_eclass;
    }
    public tgg_ContextLinkVariablePattern getTgg_contextlinkvariablepattern() {
        return tgg_contextlinkvariablepattern;
    }

    public void setTgg_contextlinkvariablepattern(tgg_ContextLinkVariablePattern tgg_contextlinkvariablepattern) {
        this.tgg_contextlinkvariablepattern = tgg_contextlinkvariablepattern;
    }

}