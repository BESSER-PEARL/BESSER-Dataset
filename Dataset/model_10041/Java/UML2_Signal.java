





import java.util.List;
import java.util.ArrayList;

public class UML2_Signal extends Classifier {






    private List<UML2_Property> uml2_propertys;




    private UML2_Reception uml2_reception;


    public UML2_Signal(
    ) {
        super(
        );
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Signal(
        ArrayList<UML2_Property> uml2_propertys    ) {
        this.uml2_propertys = uml2_propertys;
    }


    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public UML2_Reception getUml2_reception() {
        return uml2_reception;
    }

    public void setUml2_reception(UML2_Reception uml2_reception) {
        this.uml2_reception = uml2_reception;
    }

}