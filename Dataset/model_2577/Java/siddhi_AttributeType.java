





import java.util.List;
import java.util.ArrayList;

public class siddhi_AttributeType extends OBJECT, INTS, STRINGS, DOUBLE, LONG, FLOAT, BOOL {






    private siddhi_DefinitionFunction siddhi_definitionfunction;




    private siddhi_Features siddhi_features;


    public siddhi_AttributeType(
    ) {
        super(
        );
    }



    public siddhi_DefinitionFunction getSiddhi_definitionfunction() {
        return siddhi_definitionfunction;
    }

    public void setSiddhi_definitionfunction(siddhi_DefinitionFunction siddhi_definitionfunction) {
        this.siddhi_definitionfunction = siddhi_definitionfunction;
    }
    public siddhi_Features getSiddhi_features() {
        return siddhi_features;
    }

    public void setSiddhi_features(siddhi_Features siddhi_features) {
        this.siddhi_features = siddhi_features;
    }

}