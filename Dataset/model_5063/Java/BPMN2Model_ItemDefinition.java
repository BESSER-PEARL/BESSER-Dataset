





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ItemDefinition extends RootElement {

    private String itemKind;
    private boolean isCollection;



    public BPMN2Model_ItemDefinition(
        String itemKind,        boolean isCollection    ) {
        super(
        );
        this.itemKind = itemKind;
        this.isCollection = isCollection;
    }


    public String getItemkind() {
        return itemKind;
    }

    public void setItemkind(String itemKind) {
        this.itemKind = itemKind;
    }
    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }


}