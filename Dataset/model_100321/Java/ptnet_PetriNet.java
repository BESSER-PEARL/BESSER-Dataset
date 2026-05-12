





import java.util.List;
import java.util.ArrayList;

public class ptnet_PetriNet  {

    private String type;
    private String id;





    private ptnet_Name ptnet_name;




    private ptnet_PetriNetDoc ptnet_petrinetdoc;




    private ptnet_Name ptnet_name;




    private ptnet_PetriNetDoc ptnet_petrinetdoc;


    public ptnet_PetriNet(
        String type,        String id    ) {
        this.type = type;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public ptnet_Name getPtnet_name() {
        return ptnet_name;
    }

    public void setPtnet_name(ptnet_Name ptnet_name) {
        this.ptnet_name = ptnet_name;
    }
    public ptnet_PetriNetDoc getPtnet_petrinetdoc() {
        return ptnet_petrinetdoc;
    }

    public void setPtnet_petrinetdoc(ptnet_PetriNetDoc ptnet_petrinetdoc) {
        this.ptnet_petrinetdoc = ptnet_petrinetdoc;
    }
    public ptnet_Name getPtnet_name() {
        return ptnet_name;
    }

    public void setPtnet_name(ptnet_Name ptnet_name) {
        this.ptnet_name = ptnet_name;
    }
    public ptnet_PetriNetDoc getPtnet_petrinetdoc() {
        return ptnet_petrinetdoc;
    }

    public void setPtnet_petrinetdoc(ptnet_PetriNetDoc ptnet_petrinetdoc) {
        this.ptnet_petrinetdoc = ptnet_petrinetdoc;
    }

}