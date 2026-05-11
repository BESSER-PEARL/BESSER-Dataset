





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlResource extends SadlExplicitValueLiteral, Expression, SadlStatement {






    private List<sADL_SadlAnnotation> sadl_sadlannotations;




    private sADL_SadlInstance sadl_sadlinstance;




    private sADL_SadlInstance sadl_sadlinstance;




    private sADL_SadlResource sadl_sadlresource;




    private sADL_ExplainStatement sadl_explainstatement;


    public sADL_SadlResource(
    ) {
        super(
        );
        this.sadl_sadlannotations = new ArrayList<>();
    }

    public sADL_SadlResource(
        ArrayList<sADL_SadlAnnotation> sadl_sadlannotations    ) {
        this.sadl_sadlannotations = sadl_sadlannotations;
    }


    public List<sADL_SadlAnnotation> getSadl_sadlannotations() {
        return sadl_sadlannotations;
    }

    public void addSadl_sadlannotation(Sadl_sadlannotation sadl_sadlannotation) {
        this.sadl_sadlannotations.add(sadl_sadlannotation);
    }
    public sADL_SadlInstance getSadl_sadlinstance() {
        return sadl_sadlinstance;
    }

    public void setSadl_sadlinstance(sADL_SadlInstance sadl_sadlinstance) {
        this.sadl_sadlinstance = sadl_sadlinstance;
    }
    public sADL_SadlInstance getSadl_sadlinstance() {
        return sadl_sadlinstance;
    }

    public void setSadl_sadlinstance(sADL_SadlInstance sadl_sadlinstance) {
        this.sadl_sadlinstance = sadl_sadlinstance;
    }
    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public sADL_ExplainStatement getSadl_explainstatement() {
        return sadl_explainstatement;
    }

    public void setSadl_explainstatement(sADL_ExplainStatement sadl_explainstatement) {
        this.sadl_explainstatement = sadl_explainstatement;
    }

}