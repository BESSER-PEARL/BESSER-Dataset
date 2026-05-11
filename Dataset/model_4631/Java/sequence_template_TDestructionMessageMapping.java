





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TDestructionMessageMapping extends TSourceTargetMessageMapping {






    private List<TLifelineMapping> tlifelinemappings;


    public sequence_template_TDestructionMessageMapping(
    ) {
        super(
        );
        this.tlifelinemappings = new ArrayList<>();
    }

    public sequence_template_TDestructionMessageMapping(
        ArrayList<TLifelineMapping> tlifelinemappings    ) {
        this.tlifelinemappings = tlifelinemappings;
    }


    public List<TLifelineMapping> getTlifelinemappings() {
        return tlifelinemappings;
    }

    public void addTlifelinemapping(Tlifelinemapping tlifelinemapping) {
        this.tlifelinemappings.add(tlifelinemapping);
    }

}