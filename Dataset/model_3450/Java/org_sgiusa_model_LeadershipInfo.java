





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_LeadershipInfo  {

    private String manualSignedDate;
    private String lastUpdate;
    private String examPassedDate;
    private String examPassed;
    private String id;
    private String manualSigned;





    private List<LeadershipRole> leadershiproles;


    public org_sgiusa_model_LeadershipInfo(
        String manualSignedDate,        String lastUpdate,        String examPassedDate,        String examPassed,        String id,        String manualSigned    ) {
        this.manualSignedDate = manualSignedDate;
        this.lastUpdate = lastUpdate;
        this.examPassedDate = examPassedDate;
        this.examPassed = examPassed;
        this.id = id;
        this.manualSigned = manualSigned;
        this.leadershiproles = new ArrayList<>();
    }

    public org_sgiusa_model_LeadershipInfo(
        String manualSignedDate,        String lastUpdate,        String examPassedDate,        String examPassed,        String id,        String manualSigned        ArrayList<LeadershipRole> leadershiproles    ) {
        this.manualSignedDate = manualSignedDate;
        this.lastUpdate = lastUpdate;
        this.examPassedDate = examPassedDate;
        this.examPassed = examPassed;
        this.id = id;
        this.manualSigned = manualSigned;
        this.leadershiproles = leadershiproles;
    }

    public String getManualsigneddate() {
        return manualSignedDate;
    }

    public void setManualsigneddate(String manualSignedDate) {
        this.manualSignedDate = manualSignedDate;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getExampasseddate() {
        return examPassedDate;
    }

    public void setExampasseddate(String examPassedDate) {
        this.examPassedDate = examPassedDate;
    }
    public String getExampassed() {
        return examPassed;
    }

    public void setExampassed(String examPassed) {
        this.examPassed = examPassed;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getManualsigned() {
        return manualSigned;
    }

    public void setManualsigned(String manualSigned) {
        this.manualSigned = manualSigned;
    }

    public List<LeadershipRole> getLeadershiproles() {
        return leadershiproles;
    }

    public void addLeadershiprole(Leadershiprole leadershiprole) {
        this.leadershiproles.add(leadershiprole);
    }

}