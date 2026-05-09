





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_MapExp extends OclExpression {






    private EmigOcl_MapElement emigocl_mapelement;




    private List<EmigOcl_MapElement> emigocl_mapelements;


    public EmigOcl_MapExp(
    ) {
        super(
        );
        this.emigocl_mapelements = new ArrayList<>();
    }

    public EmigOcl_MapExp(
        ArrayList<EmigOcl_MapElement> emigocl_mapelements    ) {
        this.emigocl_mapelements = emigocl_mapelements;
    }


    public EmigOcl_MapElement getEmigocl_mapelement() {
        return emigocl_mapelement;
    }

    public void setEmigocl_mapelement(EmigOcl_MapElement emigocl_mapelement) {
        this.emigocl_mapelement = emigocl_mapelement;
    }
    public List<EmigOcl_MapElement> getEmigocl_mapelements() {
        return emigocl_mapelements;
    }

    public void addEmigocl_mapelement(Emigocl_mapelement emigocl_mapelement) {
        this.emigocl_mapelements.add(emigocl_mapelement);
    }

}