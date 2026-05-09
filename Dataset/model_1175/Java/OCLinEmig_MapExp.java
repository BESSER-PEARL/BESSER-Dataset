





import java.util.List;
import java.util.ArrayList;

public class OCLinEmig_MapExp extends OclExpression {






    private List<OCLinEmig_MapElement> oclinemig_mapelements;




    private OCLinEmig_MapElement oclinemig_mapelement;


    public OCLinEmig_MapExp(
    ) {
        super(
        );
        this.oclinemig_mapelements = new ArrayList<>();
    }

    public OCLinEmig_MapExp(
        ArrayList<OCLinEmig_MapElement> oclinemig_mapelements    ) {
        this.oclinemig_mapelements = oclinemig_mapelements;
    }


    public List<OCLinEmig_MapElement> getOclinemig_mapelements() {
        return oclinemig_mapelements;
    }

    public void addOclinemig_mapelement(Oclinemig_mapelement oclinemig_mapelement) {
        this.oclinemig_mapelements.add(oclinemig_mapelement);
    }
    public OCLinEmig_MapElement getOclinemig_mapelement() {
        return oclinemig_mapelement;
    }

    public void setOclinemig_mapelement(OCLinEmig_MapElement oclinemig_mapelement) {
        this.oclinemig_mapelement = oclinemig_mapelement;
    }

}