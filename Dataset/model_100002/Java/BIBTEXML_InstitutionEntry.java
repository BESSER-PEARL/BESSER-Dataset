





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_InstitutionEntry extends Entry {

    private String institution;



    public BIBTEXML_InstitutionEntry(
        String institution    ) {
        super(
        );
        this.institution = institution;
    }


    public String getInstitution() {
        return institution;
    }

    public void setInstitution(String institution) {
        this.institution = institution;
    }


}