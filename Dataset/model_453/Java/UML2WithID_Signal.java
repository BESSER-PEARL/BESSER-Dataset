





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Signal extends Classifier {






    private List<UML2WithID_Property> uml2withid_propertys;




    private UML2WithID_Reception uml2withid_reception;


    public UML2WithID_Signal(
    ) {
        super(
        );
        this.uml2withid_propertys = new ArrayList<>();
    }

    public UML2WithID_Signal(
        ArrayList<UML2WithID_Property> uml2withid_propertys    ) {
        this.uml2withid_propertys = uml2withid_propertys;
    }


    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public UML2WithID_Reception getUml2withid_reception() {
        return uml2withid_reception;
    }

    public void setUml2withid_reception(UML2WithID_Reception uml2withid_reception) {
        this.uml2withid_reception = uml2withid_reception;
    }

}