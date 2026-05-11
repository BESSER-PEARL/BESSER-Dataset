





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlRangeRestriction extends SadlPropertyRestriction {

    private String typeonly;
    private boolean singleValued;





    private sADL_SadlDataTypeFacet sadl_sadldatatypefacet;




    private sADL_SadlTypeReference sadl_sadltypereference;


    public sADL_SadlRangeRestriction(
        String typeonly,        boolean singleValued    ) {
        super(
        );
        this.typeonly = typeonly;
        this.singleValued = singleValued;
    }


    public String getTypeonly() {
        return typeonly;
    }

    public void setTypeonly(String typeonly) {
        this.typeonly = typeonly;
    }
    public boolean getSinglevalued() {
        return singleValued;
    }

    public void setSinglevalued(boolean singleValued) {
        this.singleValued = singleValued;
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