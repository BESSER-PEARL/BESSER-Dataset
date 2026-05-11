





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_StructuralComponent  {

    private String Name;





    private ORDB4ORA_Datatype ordb4ora_datatype;




    private List<ORDB4ORA_Feature> ordb4ora_features;




    private ORDB4ORA_Restriction ordb4ora_restriction;




    private List<ORDB4ORA_Restriction> ordb4ora_restrictions;


    public ORDB4ORA_StructuralComponent(
        String Name    ) {
        this.Name = Name;
        this.ordb4ora_features = new ArrayList<>();
        this.ordb4ora_restrictions = new ArrayList<>();
    }

    public ORDB4ORA_StructuralComponent(
        String Name        ArrayList<ORDB4ORA_Feature> ordb4ora_features,        ArrayList<ORDB4ORA_Restriction> ordb4ora_restrictions    ) {
        this.Name = Name;
        this.ordb4ora_features = ordb4ora_features;
        this.ordb4ora_restrictions = ordb4ora_restrictions;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public ORDB4ORA_Datatype getOrdb4ora_datatype() {
        return ordb4ora_datatype;
    }

    public void setOrdb4ora_datatype(ORDB4ORA_Datatype ordb4ora_datatype) {
        this.ordb4ora_datatype = ordb4ora_datatype;
    }
    public List<ORDB4ORA_Feature> getOrdb4ora_features() {
        return ordb4ora_features;
    }

    public void addOrdb4ora_feature(Ordb4ora_feature ordb4ora_feature) {
        this.ordb4ora_features.add(ordb4ora_feature);
    }
    public ORDB4ORA_Restriction getOrdb4ora_restriction() {
        return ordb4ora_restriction;
    }

    public void setOrdb4ora_restriction(ORDB4ORA_Restriction ordb4ora_restriction) {
        this.ordb4ora_restriction = ordb4ora_restriction;
    }
    public List<ORDB4ORA_Restriction> getOrdb4ora_restrictions() {
        return ordb4ora_restrictions;
    }

    public void addOrdb4ora_restriction(Ordb4ora_restriction ordb4ora_restriction) {
        this.ordb4ora_restrictions.add(ordb4ora_restriction);
    }

}