





import java.util.List;
import java.util.ArrayList;

public class ISO20022_EndPointCategory extends TopLevelDictionaryEntry {






    private List<ISO20022_MessageElementContainer> iso20022_messageelementcontainers;


    public ISO20022_EndPointCategory(
    ) {
        super(
        );
        this.iso20022_messageelementcontainers = new ArrayList<>();
    }

    public ISO20022_EndPointCategory(
        ArrayList<ISO20022_MessageElementContainer> iso20022_messageelementcontainers    ) {
        this.iso20022_messageelementcontainers = iso20022_messageelementcontainers;
    }


    public List<ISO20022_MessageElementContainer> getIso20022_messageelementcontainers() {
        return iso20022_messageelementcontainers;
    }

    public void addIso20022_messageelementcontainer(Iso20022_messageelementcontainer iso20022_messageelementcontainer) {
        this.iso20022_messageelementcontainers.add(iso20022_messageelementcontainer);
    }

}