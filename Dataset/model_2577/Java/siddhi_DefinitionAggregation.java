





import java.util.List;
import java.util.ArrayList;

public class siddhi_DefinitionAggregation extends FROM, BY, AGGREGATION, DEFINE, AGGREGATE {






    private siddhi_EVERY siddhi_every;




    private siddhi_StandardStream siddhi_standardstream;


    public siddhi_DefinitionAggregation(
    ) {
        super(
        );
    }



    public siddhi_EVERY getSiddhi_every() {
        return siddhi_every;
    }

    public void setSiddhi_every(siddhi_EVERY siddhi_every) {
        this.siddhi_every = siddhi_every;
    }
    public siddhi_StandardStream getSiddhi_standardstream() {
        return siddhi_standardstream;
    }

    public void setSiddhi_standardstream(siddhi_StandardStream siddhi_standardstream) {
        this.siddhi_standardstream = siddhi_standardstream;
    }

}