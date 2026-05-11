





import java.util.List;
import java.util.ArrayList;

public class delphi_reservedWord extends CSTrace {

    private String id;





    private delphi_designatorPart delphi_designatorpart;


    public delphi_reservedWord(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public delphi_designatorPart getDelphi_designatorpart() {
        return delphi_designatorpart;
    }

    public void setDelphi_designatorpart(delphi_designatorPart delphi_designatorpart) {
        this.delphi_designatorpart = delphi_designatorpart;
    }

}