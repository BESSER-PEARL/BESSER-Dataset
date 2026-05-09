





import java.util.List;
import java.util.ArrayList;

public class ASPT_TraceProp extends TraceElement {

    private String idpx;
    private String value;
    private String idp;



    public ASPT_TraceProp(
        String idpx,        String value,        String idp    ) {
        super(
        );
        this.idpx = idpx;
        this.value = value;
        this.idp = idp;
    }


    public String getIdpx() {
        return idpx;
    }

    public void setIdpx(String idpx) {
        this.idpx = idpx;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getIdp() {
        return idp;
    }

    public void setIdp(String idp) {
        this.idp = idp;
    }


}