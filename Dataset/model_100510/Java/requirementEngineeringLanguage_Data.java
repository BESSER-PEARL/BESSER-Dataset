





import java.util.List;
import java.util.ArrayList;

public class requirementEngineeringLanguage_Data  {

    private String type;
    private String locationType;
    private String quantifier;
    private String location;





    private requirementEngineeringLanguage_Given requirementengineeringlanguage_given;


    public requirementEngineeringLanguage_Data(
        String type,        String locationType,        String quantifier,        String location    ) {
        this.type = type;
        this.locationType = locationType;
        this.quantifier = quantifier;
        this.location = location;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getLocationtype() {
        return locationType;
    }

    public void setLocationtype(String locationType) {
        this.locationType = locationType;
    }
    public String getQuantifier() {
        return quantifier;
    }

    public void setQuantifier(String quantifier) {
        this.quantifier = quantifier;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public requirementEngineeringLanguage_Given getRequirementengineeringlanguage_given() {
        return requirementengineeringlanguage_given;
    }

    public void setRequirementengineeringlanguage_given(requirementEngineeringLanguage_Given requirementengineeringlanguage_given) {
        this.requirementengineeringlanguage_given = requirementengineeringlanguage_given;
    }

}