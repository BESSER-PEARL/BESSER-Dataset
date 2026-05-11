





import java.util.List;
import java.util.ArrayList;

public class cevinedit_CompartmentEReferenceCont extends PersonalizedElement {

    private boolean collapsible;
    private String layout;



    public cevinedit_CompartmentEReferenceCont(
        boolean collapsible,        String layout    ) {
        super(
        );
        this.collapsible = collapsible;
        this.layout = layout;
    }


    public boolean getCollapsible() {
        return collapsible;
    }

    public void setCollapsible(boolean collapsible) {
        this.collapsible = collapsible;
    }
    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }


}