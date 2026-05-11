





import java.util.List;
import java.util.ArrayList;

public class siddhi_AttributeReference extends SetAssignment {

    private String name;
    private String hash1;
    private String hash2;





    private siddhi_GroupBy siddhi_groupby;




    private siddhi_DefinitionAggregation siddhi_definitionaggregation;


    public siddhi_AttributeReference(
        String name,        String hash1,        String hash2    ) {
        super(
        );
        this.name = name;
        this.hash1 = hash1;
        this.hash2 = hash2;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHash1() {
        return hash1;
    }

    public void setHash1(String hash1) {
        this.hash1 = hash1;
    }
    public String getHash2() {
        return hash2;
    }

    public void setHash2(String hash2) {
        this.hash2 = hash2;
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