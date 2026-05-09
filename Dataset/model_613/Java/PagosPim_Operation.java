





import java.util.List;
import java.util.ArrayList;

public class PagosPim_Operation  {

    private String name;





    private PagosPim_GenericComponent pagospim_genericcomponent;




    private List<PagosPim_Attribute> pagospim_attributes;


    public PagosPim_Operation(
        String name    ) {
        this.name = name;
        this.pagospim_attributes = new ArrayList<>();
    }

    public PagosPim_Operation(
        String name        ArrayList<PagosPim_Attribute> pagospim_attributes    ) {
        this.name = name;
        this.pagospim_attributes = pagospim_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PagosPim_GenericComponent getPagospim_genericcomponent() {
        return pagospim_genericcomponent;
    }

    public void setPagospim_genericcomponent(PagosPim_GenericComponent pagospim_genericcomponent) {
        this.pagospim_genericcomponent = pagospim_genericcomponent;
    }
    public List<PagosPim_Attribute> getPagospim_attributes() {
        return pagospim_attributes;
    }

    public void addPagospim_attribute(Pagospim_attribute pagospim_attribute) {
        this.pagospim_attributes.add(pagospim_attribute);
    }

}