





import java.util.List;
import java.util.ArrayList;

public class library_Protocol  {

    private String name;
    private String specification;
    private String oSI;
    private String description;





    private library_Equipment library_equipment;


    public library_Protocol(
        String name,        String specification,        String oSI,        String description    ) {
        this.name = name;
        this.specification = specification;
        this.oSI = oSI;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }
    public String getOsi() {
        return oSI;
    }

    public void setOsi(String oSI) {
        this.oSI = oSI;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }

}