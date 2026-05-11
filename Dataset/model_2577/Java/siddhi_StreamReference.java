





import java.util.List;
import java.util.ArrayList;

public class siddhi_StreamReference  {

    private String hash;





    private siddhi_Name siddhi_name;




    private siddhi_NullCheck siddhi_nullcheck;




    private siddhi_AttributeIndex siddhi_attributeindex;


    public siddhi_StreamReference(
        String hash    ) {
        this.hash = hash;
    }


    public String getHash() {
        return hash;
    }

    public void setHash(String hash) {
        this.hash = hash;
    }

    public siddhi_Name getSiddhi_name() {
        return siddhi_name;
    }

    public void setSiddhi_name(siddhi_Name siddhi_name) {
        this.siddhi_name = siddhi_name;
    }
    public siddhi_NullCheck getSiddhi_nullcheck() {
        return siddhi_nullcheck;
    }

    public void setSiddhi_nullcheck(siddhi_NullCheck siddhi_nullcheck) {
        this.siddhi_nullcheck = siddhi_nullcheck;
    }
    public siddhi_AttributeIndex getSiddhi_attributeindex() {
        return siddhi_attributeindex;
    }

    public void setSiddhi_attributeindex(siddhi_AttributeIndex siddhi_attributeindex) {
        this.siddhi_attributeindex = siddhi_attributeindex;
    }

}