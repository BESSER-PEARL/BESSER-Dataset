





import java.util.List;
import java.util.ArrayList;

public class carnot_XmlTextNode  {

    private String mixed;





    private carnot_AttributeType carnot_attributetype;




    private carnot_TransitionType carnot_transitiontype;


    public carnot_XmlTextNode(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public carnot_AttributeType getCarnot_attributetype() {
        return carnot_attributetype;
    }

    public void setCarnot_attributetype(carnot_AttributeType carnot_attributetype) {
        this.carnot_attributetype = carnot_attributetype;
    }
    public carnot_TransitionType getCarnot_transitiontype() {
        return carnot_transitiontype;
    }

    public void setCarnot_transitiontype(carnot_TransitionType carnot_transitiontype) {
        this.carnot_transitiontype = carnot_transitiontype;
    }

}