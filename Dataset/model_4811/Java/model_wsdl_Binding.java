





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Binding extends wsdl_IBinding, wsdl_ExtensibleElement {

    private String qName;
    private boolean undefined;





    private PortType porttype;


    public model_wsdl_Binding(
        String qName,        boolean undefined    ) {
        super(
        );
        this.qName = qName;
        this.undefined = undefined;
    }


    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }
    public boolean getUndefined() {
        return undefined;
    }

    public void setUndefined(boolean undefined) {
        this.undefined = undefined;
    }

    public PortType getPorttype() {
        return porttype;
    }

    public void setPorttype(PortType porttype) {
        this.porttype = porttype;
    }

}