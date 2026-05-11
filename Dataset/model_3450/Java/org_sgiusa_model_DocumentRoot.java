





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_DocumentRoot  {

    private String mixed;





    private List<GohonzonInfo> gohonzoninfos;




    private List<EmailList> emaillists;




    private List<FamilyMember> familymembers;


    public org_sgiusa_model_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.gohonzoninfos = new ArrayList<>();
        this.emaillists = new ArrayList<>();
        this.familymembers = new ArrayList<>();
    }

    public org_sgiusa_model_DocumentRoot(
        String mixed        ArrayList<GohonzonInfo> gohonzoninfos,        ArrayList<EmailList> emaillists,        ArrayList<FamilyMember> familymembers    ) {
        this.mixed = mixed;
        this.gohonzoninfos = gohonzoninfos;
        this.emaillists = emaillists;
        this.familymembers = familymembers;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<GohonzonInfo> getGohonzoninfos() {
        return gohonzoninfos;
    }

    public void addGohonzoninfo(Gohonzoninfo gohonzoninfo) {
        this.gohonzoninfos.add(gohonzoninfo);
    }
    public List<EmailList> getEmaillists() {
        return emaillists;
    }

    public void addEmaillist(Emaillist emaillist) {
        this.emaillists.add(emaillist);
    }
    public List<FamilyMember> getFamilymembers() {
        return familymembers;
    }

    public void addFamilymember(Familymember familymember) {
        this.familymembers.add(familymember);
    }

}