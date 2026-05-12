





import java.util.List;
import java.util.ArrayList;

public class pnml_Element  {

    private String id;
    private String location;





    private pnml_NetElement pnml_netelement;


    public pnml_Element(
        String id,        String location    ) {
        this.id = id;
        this.location = location;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public pnml_NetElement getPnml_netelement() {
        return pnml_netelement;
    }

    public void setPnml_netelement(pnml_NetElement pnml_netelement) {
        this.pnml_netelement = pnml_netelement;
    }

}