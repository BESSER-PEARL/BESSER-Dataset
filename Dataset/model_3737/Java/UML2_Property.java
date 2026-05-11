





import java.util.List;
import java.util.ArrayList;

public class UML2_Property  {






    private UML2_LinkEndData uml2_linkenddata;




    private List<UML2_Property> uml2_propertys;


    public UML2_Property(
    ) {
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Property(
        ArrayList<UML2_Property> uml2_propertys    ) {
        this.uml2_propertys = uml2_propertys;
    }


    public UML2_LinkEndData getUml2_linkenddata() {
        return uml2_linkenddata;
    }

    public void setUml2_linkenddata(UML2_LinkEndData uml2_linkenddata) {
        this.uml2_linkenddata = uml2_linkenddata;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }

}