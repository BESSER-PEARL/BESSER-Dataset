





import java.util.List;
import java.util.ArrayList;

public class astm_TypesCatchBlock extends CatchBlock {






    private List<astm_Type> astm_types;


    public astm_TypesCatchBlock(
    ) {
        super(
        );
        this.astm_types = new ArrayList<>();
    }

    public astm_TypesCatchBlock(
        ArrayList<astm_Type> astm_types    ) {
        this.astm_types = astm_types;
    }


    public List<astm_Type> getAstm_types() {
        return astm_types;
    }

    public void addAstm_type(Astm_type astm_type) {
        this.astm_types.add(astm_type);
    }

}