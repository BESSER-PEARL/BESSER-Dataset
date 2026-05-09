





import java.util.List;
import java.util.ArrayList;

public class PagosPim_Attribute extends AttributeDefinition {

    private String isIndex;





    private PagosPim_GenericComponent pagospim_genericcomponent;


    public PagosPim_Attribute(
        String isIndex    ) {
        super(
        );
        this.isIndex = isIndex;
    }


    public String getIsindex() {
        return isIndex;
    }

    public void setIsindex(String isIndex) {
        this.isIndex = isIndex;
    }

    public PagosPim_GenericComponent getPagospim_genericcomponent() {
        return pagospim_genericcomponent;
    }

    public void setPagospim_genericcomponent(PagosPim_GenericComponent pagospim_genericcomponent) {
        this.pagospim_genericcomponent = pagospim_genericcomponent;
    }

}