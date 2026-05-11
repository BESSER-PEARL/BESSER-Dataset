





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlCardinalityCondition extends SadlCondition {

    private String cardinality;
    private String operator;





    private sADL_SadlDataTypeFacet sadl_sadldatatypefacet;




    private sADL_SadlTypeReference sadl_sadltypereference;


    public sADL_SadlCardinalityCondition(
        String cardinality,        String operator    ) {
        super(
        );
        this.cardinality = cardinality;
        this.operator = operator;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public sADL_SadlDataTypeFacet getSadl_sadldatatypefacet() {
        return sadl_sadldatatypefacet;
    }

    public void setSadl_sadldatatypefacet(sADL_SadlDataTypeFacet sadl_sadldatatypefacet) {
        this.sadl_sadldatatypefacet = sadl_sadldatatypefacet;
    }
    public sADL_SadlTypeReference getSadl_sadltypereference() {
        return sadl_sadltypereference;
    }

    public void setSadl_sadltypereference(sADL_SadlTypeReference sadl_sadltypereference) {
        this.sadl_sadltypereference = sadl_sadltypereference;
    }

}