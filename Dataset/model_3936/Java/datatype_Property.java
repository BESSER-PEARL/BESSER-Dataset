





import java.util.List;
import java.util.ArrayList;

public class datatype_Property  {

    private String description;
    private boolean multiplicity;
    private String name;
    private boolean extension;



    public datatype_Property(
        String description,        boolean multiplicity,        String name,        boolean extension    ) {
        this.description = description;
        this.multiplicity = multiplicity;
        this.name = name;
        this.extension = extension;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(boolean multiplicity) {
        this.multiplicity = multiplicity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getExtension() {
        return extension;
    }

    public void setExtension(boolean extension) {
        this.extension = extension;
    }


}