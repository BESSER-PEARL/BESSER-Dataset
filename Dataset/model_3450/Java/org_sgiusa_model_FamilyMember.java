





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_FamilyMember  {

    private String id;
    private String familyRelation;
    private String sgiMember;
    private String personName;
    private String lastUpdate;



    public org_sgiusa_model_FamilyMember(
        String id,        String familyRelation,        String sgiMember,        String personName,        String lastUpdate    ) {
        this.id = id;
        this.familyRelation = familyRelation;
        this.sgiMember = sgiMember;
        this.personName = personName;
        this.lastUpdate = lastUpdate;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFamilyrelation() {
        return familyRelation;
    }

    public void setFamilyrelation(String familyRelation) {
        this.familyRelation = familyRelation;
    }
    public String getSgimember() {
        return sgiMember;
    }

    public void setSgimember(String sgiMember) {
        this.sgiMember = sgiMember;
    }
    public String getPersonname() {
        return personName;
    }

    public void setPersonname(String personName) {
        this.personName = personName;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }


}