





import java.util.List;
import java.util.ArrayList;

public class dsl_RestPart  {

    private String partName;
    private String partData;





    private dsl_Rest dsl_rest;


    public dsl_RestPart(
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

    public dsl_Rest getDsl_rest() {
        return dsl_rest;
    }

    public void setDsl_rest(dsl_Rest dsl_rest) {
        this.dsl_rest = dsl_rest;
    }

}