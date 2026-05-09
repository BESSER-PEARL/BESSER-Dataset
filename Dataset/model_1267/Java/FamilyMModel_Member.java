





import java.util.List;
import java.util.ArrayList;

public class FamilyMModel_Member  {

    private String relation;
    private String firstName;





    private FamilyMModel_Family familymmodel_family;


    public FamilyMModel_Member(
        String relation,        String firstName    ) {
        this.relation = relation;
        this.firstName = firstName;
    }


    public String getRelation() {
        return relation;
    }

    public void setRelation(String relation) {
        this.relation = relation;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public FamilyMModel_Family getFamilymmodel_family() {
        return familymmodel_family;
    }

    public void setFamilymmodel_family(FamilyMModel_Family familymmodel_family) {
        this.familymmodel_family = familymmodel_family;
    }

}