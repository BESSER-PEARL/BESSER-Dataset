





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETSpecificationInstantiation extends ETSpecificationExpression {






    private ecdarText_ETSpecificationTemplate ecdartext_etspecificationtemplate;




    private List<ecdarText_ETExpression> ecdartext_etexpressions;


    public ecdarText_ETSpecificationInstantiation(
    ) {
        super(
        );
        this.ecdartext_etexpressions = new ArrayList<>();
    }

    public ecdarText_ETSpecificationInstantiation(
        ArrayList<ecdarText_ETExpression> ecdartext_etexpressions    ) {
        this.ecdartext_etexpressions = ecdartext_etexpressions;
    }


    public ecdarText_ETSpecificationTemplate getEcdartext_etspecificationtemplate() {
        return ecdartext_etspecificationtemplate;
    }

    public void setEcdartext_etspecificationtemplate(ecdarText_ETSpecificationTemplate ecdartext_etspecificationtemplate) {
        this.ecdartext_etspecificationtemplate = ecdartext_etspecificationtemplate;
    }
    public List<ecdarText_ETExpression> getEcdartext_etexpressions() {
        return ecdartext_etexpressions;
    }

    public void addEcdartext_etexpression(Ecdartext_etexpression ecdartext_etexpression) {
        this.ecdartext_etexpressions.add(ecdartext_etexpression);
    }

}