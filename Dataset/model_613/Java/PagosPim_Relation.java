





import java.util.List;
import java.util.ArrayList;

public class PagosPim_Relation  {

    private String name;
    private String type;
    private String cardinality;





    private PagosPim_GenericComponent pagospim_genericcomponent;




    private PagosPim_GenericComponent pagospim_genericcomponent;


    public PagosPim_Relation(
        String name,        String type,        String cardinality    ) {
        this.name = name;
        this.type = type;
        this.cardinality = cardinality;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }

    public PagosPim_GenericComponent getPagospim_genericcomponent() {
        return pagospim_genericcomponent;
    }

    public void setPagospim_genericcomponent(PagosPim_GenericComponent pagospim_genericcomponent) {
        this.pagospim_genericcomponent = pagospim_genericcomponent;
    }
    public PagosPim_GenericComponent getPagospim_genericcomponent() {
        return pagospim_genericcomponent;
    }

    public void setPagospim_genericcomponent(PagosPim_GenericComponent pagospim_genericcomponent) {
        this.pagospim_genericcomponent = pagospim_genericcomponent;
    }

}