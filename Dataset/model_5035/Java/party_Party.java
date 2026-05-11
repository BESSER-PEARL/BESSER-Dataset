





import java.util.List;
import java.util.ArrayList;

public class party_Party extends Tagged {

    private String uid;
    private String name;





    private List<party_ContactInfo> party_contactinfos;




    private party_Organization party_organization;




    private party_Organization party_organization;




    private party_ContactInfo party_contactinfo;




    private List<party_Identity> party_identitys;




    private party_Organization party_organization;




    private party_Role party_role;




    private party_MatrixRelationship party_matrixrelationship;


    public party_Party(
        String uid,        String name    ) {
        super(
        );
        this.uid = uid;
        this.name = name;
        this.party_contactinfos = new ArrayList<>();
        this.party_identitys = new ArrayList<>();
    }

    public party_Party(
        String uid,        String name        ArrayList<party_ContactInfo> party_contactinfos,        ArrayList<party_Identity> party_identitys    ) {
        this.uid = uid;
        this.name = name;
        this.party_contactinfos = party_contactinfos;
        this.party_identitys = party_identitys;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<party_ContactInfo> getParty_contactinfos() {
        return party_contactinfos;
    }

    public void addParty_contactinfo(Party_contactinfo party_contactinfo) {
        this.party_contactinfos.add(party_contactinfo);
    }
    public party_Organization getParty_organization() {
        return party_organization;
    }

    public void setParty_organization(party_Organization party_organization) {
        this.party_organization = party_organization;
    }
    public party_Organization getParty_organization() {
        return party_organization;
    }

    public void setParty_organization(party_Organization party_organization) {
        this.party_organization = party_organization;
    }
    public party_ContactInfo getParty_contactinfo() {
        return party_contactinfo;
    }

    public void setParty_contactinfo(party_ContactInfo party_contactinfo) {
        this.party_contactinfo = party_contactinfo;
    }
    public List<party_Identity> getParty_identitys() {
        return party_identitys;
    }

    public void addParty_identity(Party_identity party_identity) {
        this.party_identitys.add(party_identity);
    }
    public party_Organization getParty_organization() {
        return party_organization;
    }

    public void setParty_organization(party_Organization party_organization) {
        this.party_organization = party_organization;
    }
    public party_Role getParty_role() {
        return party_role;
    }

    public void setParty_role(party_Role party_role) {
        this.party_role = party_role;
    }
    public party_MatrixRelationship getParty_matrixrelationship() {
        return party_matrixrelationship;
    }

    public void setParty_matrixrelationship(party_MatrixRelationship party_matrixrelationship) {
        this.party_matrixrelationship = party_matrixrelationship;
    }

}