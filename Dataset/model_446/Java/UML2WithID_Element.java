





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Element  {

    private String ID;





    private UML2WithID_Element uml2withid_element;


    public UML2WithID_Element(
        String ID    ) {
        this.ID = ID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public UML2WithID_Element getUml2withid_element() {
        return uml2withid_element;
    }

    public void setUml2withid_element(UML2WithID_Element uml2withid_element) {
        this.uml2withid_element = uml2withid_element;
    }

}