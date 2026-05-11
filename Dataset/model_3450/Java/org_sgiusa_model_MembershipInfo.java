





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_MembershipInfo  {

    private String friendOfSgi;
    private String receivedCertificate;
    private String lastUpdate;
    private String notLocatable;
    private String id;
    private String notActivated;





    private List<GohonzonInfo> gohonzoninfos;


    public org_sgiusa_model_MembershipInfo(
        String friendOfSgi,        String receivedCertificate,        String lastUpdate,        String notLocatable,        String id,        String notActivated    ) {
        this.friendOfSgi = friendOfSgi;
        this.receivedCertificate = receivedCertificate;
        this.lastUpdate = lastUpdate;
        this.notLocatable = notLocatable;
        this.id = id;
        this.notActivated = notActivated;
        this.gohonzoninfos = new ArrayList<>();
    }

    public org_sgiusa_model_MembershipInfo(
        String friendOfSgi,        String receivedCertificate,        String lastUpdate,        String notLocatable,        String id,        String notActivated        ArrayList<GohonzonInfo> gohonzoninfos    ) {
        this.friendOfSgi = friendOfSgi;
        this.receivedCertificate = receivedCertificate;
        this.lastUpdate = lastUpdate;
        this.notLocatable = notLocatable;
        this.id = id;
        this.notActivated = notActivated;
        this.gohonzoninfos = gohonzoninfos;
    }

    public String getFriendofsgi() {
        return friendOfSgi;
    }

    public void setFriendofsgi(String friendOfSgi) {
        this.friendOfSgi = friendOfSgi;
    }
    public String getReceivedcertificate() {
        return receivedCertificate;
    }

    public void setReceivedcertificate(String receivedCertificate) {
        this.receivedCertificate = receivedCertificate;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getNotlocatable() {
        return notLocatable;
    }

    public void setNotlocatable(String notLocatable) {
        this.notLocatable = notLocatable;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNotactivated() {
        return notActivated;
    }

    public void setNotactivated(String notActivated) {
        this.notActivated = notActivated;
    }

    public List<GohonzonInfo> getGohonzoninfos() {
        return gohonzoninfos;
    }

    public void addGohonzoninfo(Gohonzoninfo gohonzoninfo) {
        this.gohonzoninfos.add(gohonzoninfo);
    }

}