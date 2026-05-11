





import java.util.List;
import java.util.ArrayList;

public class sparrow_RestPart  {

    private String partName;
    private String partData;





    private sparrow_Rest sparrow_rest;


    public sparrow_RestPart(
        String partName,        String partData    ) {
        this.partName = partName;
        this.partData = partData;
    }


    public String getPartname() {
        return partName;
    }

    public void setPartname(String partName) {
        this.partName = partName;
    }
    public String getPartdata() {
        return partData;
    }

    public void setPartdata(String partData) {
        this.partData = partData;
    }

    public sparrow_Rest getSparrow_rest() {
        return sparrow_rest;
    }

    public void setSparrow_rest(sparrow_Rest sparrow_rest) {
        this.sparrow_rest = sparrow_rest;
    }

}