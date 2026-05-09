





import java.util.List;
import java.util.ArrayList;

public class uma_WorkOrder extends ProcessElement {

    private String linkType;



    public uma_WorkOrder(
        String linkType    ) {
        super(
        );
        this.linkType = linkType;
    }


    public String getLinktype() {
        return linkType;
    }

    public void setLinktype(String linkType) {
        this.linkType = linkType;
    }


}