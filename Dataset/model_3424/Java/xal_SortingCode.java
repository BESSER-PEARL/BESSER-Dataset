





import java.util.List;
import java.util.ArrayList;

public class xal_SortingCode  {

    private String code;
    private String type;





    private xal_PostalServiceElements xal_postalserviceelements;


    public xal_SortingCode(
        String code,        String type    ) {
        this.code = code;
        this.type = type;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_PostalServiceElements getXal_postalserviceelements() {
        return xal_postalserviceelements;
    }

    public void setXal_postalserviceelements(xal_PostalServiceElements xal_postalserviceelements) {
        this.xal_postalserviceelements = xal_postalserviceelements;
    }

}