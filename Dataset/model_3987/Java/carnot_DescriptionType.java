





import java.util.List;
import java.util.ArrayList;

public class carnot_DescriptionType  {

    private String mixed;





    private carnot_ContextType carnot_contexttype;




    private carnot_IIdentifiableModelElement carnot_iidentifiablemodelelement;




    private carnot_ModelType carnot_modeltype;




    private carnot_ViewType carnot_viewtype;


    public carnot_DescriptionType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public carnot_ContextType getCarnot_contexttype() {
        return carnot_contexttype;
    }

    public void setCarnot_contexttype(carnot_ContextType carnot_contexttype) {
        this.carnot_contexttype = carnot_contexttype;
    }
    public carnot_IIdentifiableModelElement getCarnot_iidentifiablemodelelement() {
        return carnot_iidentifiablemodelelement;
    }

    public void setCarnot_iidentifiablemodelelement(carnot_IIdentifiableModelElement carnot_iidentifiablemodelelement) {
        this.carnot_iidentifiablemodelelement = carnot_iidentifiablemodelelement;
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public carnot_ViewType getCarnot_viewtype() {
        return carnot_viewtype;
    }

    public void setCarnot_viewtype(carnot_ViewType carnot_viewtype) {
        this.carnot_viewtype = carnot_viewtype;
    }

}