





import java.util.List;
import java.util.ArrayList;

public class model_Content  {

    private String uniqueAttribute;
    private String secondAttribute;





    private model_Container model_container;


    public model_Content(
        String uniqueAttribute,        String secondAttribute    ) {
        this.uniqueAttribute = uniqueAttribute;
        this.secondAttribute = secondAttribute;
    }


    public String getUniqueattribute() {
        return uniqueAttribute;
    }

    public void setUniqueattribute(String uniqueAttribute) {
        this.uniqueAttribute = uniqueAttribute;
    }
    public String getSecondattribute() {
        return secondAttribute;
    }

    public void setSecondattribute(String secondAttribute) {
        this.secondAttribute = secondAttribute;
    }

    public model_Container getModel_container() {
        return model_container;
    }

    public void setModel_container(model_Container model_container) {
        this.model_container = model_container;
    }

}