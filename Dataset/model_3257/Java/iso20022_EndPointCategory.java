





import java.util.List;
import java.util.ArrayList;

public class iso20022_EndPointCategory extends TopLevelDictionaryEntry {






    private List<iso20022_MessageElementContainer> iso20022_messageelementcontainers;


    public iso20022_EndPointCategory(
    ) {
        super(
        );
        this.iso20022_messageelementcontainers = new ArrayList<>();
    }

    public iso20022_EndPointCategory(
        ArrayList<iso20022_MessageElementContainer> iso20022_messageelementcontainers    ) {
        this.iso20022_messageelementcontainers = iso20022_messageelementcontainers;
    }


    public List<iso20022_MessageElementContainer> getIso20022_messageelementcontainers() {
        return iso20022_messageelementcontainers;
    }

    public void addIso20022_messageelementcontainer(Iso20022_messageelementcontainer iso20022_messageelementcontainer) {
        this.iso20022_messageelementcontainers.add(iso20022_messageelementcontainer);
    }

}