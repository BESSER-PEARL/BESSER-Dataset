





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Section extends LocatedElement {

    private String sectionType;





    private List<MappingElement> mappingelements;


    public frontend_mappings_Section(
        String sectionType    ) {
        super(
        );
        this.sectionType = sectionType;
        this.mappingelements = new ArrayList<>();
    }

    public frontend_mappings_Section(
        String sectionType        ArrayList<MappingElement> mappingelements    ) {
        this.sectionType = sectionType;
        this.mappingelements = mappingelements;
    }

    public String getSectiontype() {
        return sectionType;
    }

    public void setSectiontype(String sectionType) {
        this.sectionType = sectionType;
    }

    public List<MappingElement> getMappingelements() {
        return mappingelements;
    }

    public void addMappingelement(Mappingelement mappingelement) {
        this.mappingelements.add(mappingelement);
    }

}