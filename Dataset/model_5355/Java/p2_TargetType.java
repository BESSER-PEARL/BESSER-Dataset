





import java.util.List;
import java.util.ArrayList;

public class p2_TargetType  {

    private String name;
    private String sequenceNumber;





    private p2_DocumentRoot p2_documentroot;


    public p2_TargetType(
        String name,        String sequenceNumber    ) {
        this.name = name;
        this.sequenceNumber = sequenceNumber;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSequencenumber() {
        return sequenceNumber;
    }

    public void setSequencenumber(String sequenceNumber) {
        this.sequenceNumber = sequenceNumber;
    }

    public p2_DocumentRoot getP2_documentroot() {
        return p2_documentroot;
    }

    public void setP2_documentroot(p2_DocumentRoot p2_documentroot) {
        this.p2_documentroot = p2_documentroot;
    }

}