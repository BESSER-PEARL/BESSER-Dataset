





import java.util.List;
import java.util.ArrayList;

public class uml2CD_DirectRelationship extends Relationship {






    private List<uml2CD_Element> uml2cd_elements;




    private List<uml2CD_Element> uml2cd_elements;


    public uml2CD_DirectRelationship(
    ) {
        super(
        );
        this.uml2cd_elements = new ArrayList<>();
        this.uml2cd_elements = new ArrayList<>();
    }

    public uml2CD_DirectRelationship(
        ArrayList<uml2CD_Element> uml2cd_elements,        ArrayList<uml2CD_Element> uml2cd_elements    ) {
        this.uml2cd_elements = uml2cd_elements;
        this.uml2cd_elements = uml2cd_elements;
    }


    public List<uml2CD_Element> getUml2cd_elements() {
        return uml2cd_elements;
    }

    public void addUml2cd_element(Uml2cd_element uml2cd_element) {
        this.uml2cd_elements.add(uml2cd_element);
    }
    public List<uml2CD_Element> getUml2cd_elements() {
        return uml2cd_elements;
    }

    public void addUml2cd_element(Uml2cd_element uml2cd_element) {
        this.uml2cd_elements.add(uml2cd_element);
    }

}