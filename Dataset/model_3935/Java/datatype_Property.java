





import java.util.List;
import java.util.ArrayList;

public class datatype_Property  {

    private String description;
    private String name;
    private boolean multiplicity;





    private datatype_Entity datatype_entity;


    public datatype_Property(
        String description,        String name,        boolean multiplicity    ) {
        this.description = description;
        this.name = name;
        this.multiplicity = multiplicity;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(boolean multiplicity) {
        this.multiplicity = multiplicity;
    }

    public datatype_Entity getDatatype_entity() {
        return datatype_entity;
    }

    public void setDatatype_entity(datatype_Entity datatype_entity) {
        this.datatype_entity = datatype_entity;
    }

}