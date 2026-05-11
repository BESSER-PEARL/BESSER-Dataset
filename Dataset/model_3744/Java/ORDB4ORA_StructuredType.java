





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_StructuredType extends Datatype {

    private String Name;
    private boolean is_final;
    private boolean is_instantiable;





    private ORDB4ORA_StructuredType ordb4ora_structuredtype;




    private List<ORDB4ORA_Attribute> ordb4ora_attributes;




    private ORDB4ORA_Attribute ordb4ora_attribute;


    public ORDB4ORA_StructuredType(
        String Name,        boolean is_final,        boolean is_instantiable    ) {
        super(
        );
        this.Name = Name;
        this.is_final = is_final;
        this.is_instantiable = is_instantiable;
        this.ordb4ora_attributes = new ArrayList<>();
    }

    public ORDB4ORA_StructuredType(
        String Name,        boolean is_final,        boolean is_instantiable        ArrayList<ORDB4ORA_Attribute> ordb4ora_attributes    ) {
        this.Name = Name;
        this.is_final = is_final;
        this.is_instantiable = is_instantiable;
        this.ordb4ora_attributes = ordb4ora_attributes;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getIs_final() {
        return is_final;
    }

    public void setIs_final(boolean is_final) {
        this.is_final = is_final;
    }
    public boolean getIs_instantiable() {
        return is_instantiable;
    }

    public void setIs_instantiable(boolean is_instantiable) {
        this.is_instantiable = is_instantiable;
    }

    public ORDB4ORA_StructuredType getOrdb4ora_structuredtype() {
        return ordb4ora_structuredtype;
    }

    public void setOrdb4ora_structuredtype(ORDB4ORA_StructuredType ordb4ora_structuredtype) {
        this.ordb4ora_structuredtype = ordb4ora_structuredtype;
    }
    public List<ORDB4ORA_Attribute> getOrdb4ora_attributes() {
        return ordb4ora_attributes;
    }

    public void addOrdb4ora_attribute(Ordb4ora_attribute ordb4ora_attribute) {
        this.ordb4ora_attributes.add(ordb4ora_attribute);
    }
    public ORDB4ORA_Attribute getOrdb4ora_attribute() {
        return ordb4ora_attribute;
    }

    public void setOrdb4ora_attribute(ORDB4ORA_Attribute ordb4ora_attribute) {
        this.ordb4ora_attribute = ordb4ora_attribute;
    }

}