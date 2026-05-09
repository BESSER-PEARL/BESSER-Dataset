





import java.util.List;
import java.util.ArrayList;

public class simpleocl_MapExp extends OclExpression {






    private simpleocl_MapElement simpleocl_mapelement;




    private List<simpleocl_MapElement> simpleocl_mapelements;


    public simpleocl_MapExp(
    ) {
        super(
        );
        this.simpleocl_mapelements = new ArrayList<>();
    }

    public simpleocl_MapExp(
        ArrayList<simpleocl_MapElement> simpleocl_mapelements    ) {
        this.simpleocl_mapelements = simpleocl_mapelements;
    }


    public simpleocl_MapElement getSimpleocl_mapelement() {
        return simpleocl_mapelement;
    }

    public void setSimpleocl_mapelement(simpleocl_MapElement simpleocl_mapelement) {
        this.simpleocl_mapelement = simpleocl_mapelement;
    }
    public List<simpleocl_MapElement> getSimpleocl_mapelements() {
        return simpleocl_mapelements;
    }

    public void addSimpleocl_mapelement(Simpleocl_mapelement simpleocl_mapelement) {
        this.simpleocl_mapelements.add(simpleocl_mapelement);
    }

}