





import java.util.List;
import java.util.ArrayList;

public class delphi_designatorPart extends CSTrace {

    private String id2;
    private String id;





    private delphi_designatorSubPart delphi_designatorsubpart;


    public delphi_designatorPart(
        String id2,        String id    ) {
        super(
        );
        this.id2 = id2;
        this.id = id;
    }


    public String getId2() {
        return id2;
    }

    public void setId2(String id2) {
        this.id2 = id2;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public delphi_designatorSubPart getDelphi_designatorsubpart() {
        return delphi_designatorsubpart;
    }

    public void setDelphi_designatorsubpart(delphi_designatorSubPart delphi_designatorsubpart) {
        this.delphi_designatorsubpart = delphi_designatorsubpart;
    }

}