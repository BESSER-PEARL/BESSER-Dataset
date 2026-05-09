





import java.util.List;
import java.util.ArrayList;

public class qvtrelation_cst_RelationCS extends CSTNode {

    private boolean top;





    private List<AbstractDomainCS> abstractdomaincss;


    public qvtrelation_cst_RelationCS(
        boolean top    ) {
        super(
        );
        this.top = top;
        this.abstractdomaincss = new ArrayList<>();
    }

    public qvtrelation_cst_RelationCS(
        boolean top        ArrayList<AbstractDomainCS> abstractdomaincss    ) {
        this.top = top;
        this.abstractdomaincss = abstractdomaincss;
    }

    public boolean getTop() {
        return top;
    }

    public void setTop(boolean top) {
        this.top = top;
    }

    public List<AbstractDomainCS> getAbstractdomaincss() {
        return abstractdomaincss;
    }

    public void addAbstractdomaincs(Abstractdomaincs abstractdomaincs) {
        this.abstractdomaincss.add(abstractdomaincs);
    }

}