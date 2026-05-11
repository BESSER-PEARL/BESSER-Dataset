





import java.util.List;
import java.util.ArrayList;

public class ecvi_Accession  {

    private String infieldTest;
    private String id;



    public ecvi_Accession(
        String infieldTest,        String id    ) {
        this.infieldTest = infieldTest;
        this.id = id;
    }


    public String getInfieldtest() {
        return infieldTest;
    }

    public void setInfieldtest(String infieldTest) {
        this.infieldTest = infieldTest;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}