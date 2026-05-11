





import java.util.List;
import java.util.ArrayList;

public class siddhi_GroupByQuerySelection extends SELECT {






    private siddhi_GroupBy siddhi_groupby;




    private siddhi_DefinitionAggregation siddhi_definitionaggregation;


    public siddhi_GroupByQuerySelection(
    ) {
        super(
        );
    }



    public siddhi_GroupBy getSiddhi_groupby() {
        return siddhi_groupby;
    }

    public void setSiddhi_groupby(siddhi_GroupBy siddhi_groupby) {
        this.siddhi_groupby = siddhi_groupby;
    }
    public siddhi_DefinitionAggregation getSiddhi_definitionaggregation() {
        return siddhi_definitionaggregation;
    }

    public void setSiddhi_definitionaggregation(siddhi_DefinitionAggregation siddhi_definitionaggregation) {
        this.siddhi_definitionaggregation = siddhi_definitionaggregation;
    }

}