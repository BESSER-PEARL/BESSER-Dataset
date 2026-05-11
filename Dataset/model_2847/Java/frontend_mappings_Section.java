





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Section extends LocatedElement {

    private String sectionType;



    public frontend_mappings_Section(
        String sectionType    ) {
        super(
        );
        this.sectionType = sectionType;
    }


    public String getSectiontype() {
        return sectionType;
    }

    public void setSectiontype(String sectionType) {
        this.sectionType = sectionType;
    }


}