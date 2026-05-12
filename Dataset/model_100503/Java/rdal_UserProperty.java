





import java.util.List;
import java.util.ArrayList;

public class rdal_UserProperty  {

    private String value;
    private String name;





    private rdal_IdentifiedElement rdal_identifiedelement;


    public rdal_UserProperty(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdal_IdentifiedElement getRdal_identifiedelement() {
        return rdal_identifiedelement;
    }

    public void setRdal_identifiedelement(rdal_IdentifiedElement rdal_identifiedelement) {
        this.rdal_identifiedelement = rdal_identifiedelement;
    }

}