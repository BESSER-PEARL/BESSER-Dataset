





import java.util.List;
import java.util.ArrayList;

public class sADL_AbstractSadlEquation  {

    private String unknown;





    private sADL_SadlTypeReference sadl_sadltypereference;




    private sADL_SadlResource sadl_sadlresource;


    public sADL_AbstractSadlEquation(
        String unknown    ) {
        this.unknown = unknown;
    }


    public String getUnknown() {
        return unknown;
    }

    public void setUnknown(String unknown) {
        this.unknown = unknown;
    }

    public sADL_SadlTypeReference getSadl_sadltypereference() {
        return sadl_sadltypereference;
    }

    public void setSadl_sadltypereference(sADL_SadlTypeReference sadl_sadltypereference) {
        this.sadl_sadltypereference = sadl_sadltypereference;
    }
    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }

}