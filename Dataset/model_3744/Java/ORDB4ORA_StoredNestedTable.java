





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_StoredNestedTable  {

    private String Name;





    private ORDB4ORA_Attribute ordb4ora_attribute;


    public ORDB4ORA_StoredNestedTable(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public ORDB4ORA_Attribute getOrdb4ora_attribute() {
        return ordb4ora_attribute;
    }

    public void setOrdb4ora_attribute(ORDB4ORA_Attribute ordb4ora_attribute) {
        this.ordb4ora_attribute = ordb4ora_attribute;
    }

}