





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Service extends wsdl_IService, wsdl_ExtensibleElement {

    private String qName;
    private boolean undefined;



    public model_wsdl_Service(
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


}