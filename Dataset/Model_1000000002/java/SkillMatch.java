




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class SkillMatch  {

    private None status;
    private LocalDate startDate;
    private LocalDate createdDate;
    private int matchId;





    private List<SkillRequest> skillrequests;


    public SkillMatch(
        None status,        LocalDate startDate,        LocalDate createdDate,        int matchId    ) {
        this.status = status;
        this.startDate = startDate;
        this.createdDate = createdDate;
        this.matchId = matchId;
        this.skillrequests = new ArrayList<>();
    }

    public SkillMatch(
        None status,        LocalDate startDate,        LocalDate createdDate,        int matchId        ArrayList<SkillRequest> skillrequests    ) {
        this.status = status;
        this.startDate = startDate;
        this.createdDate = createdDate;
        this.matchId = matchId;
        this.skillrequests = skillrequests;
    }

    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getCreateddate() {
        return createdDate;
    }

    public void setCreateddate(LocalDate createdDate) {
        this.createdDate = createdDate;
    }
    public int getMatchid() {
        return matchId;
    }

    public void setMatchid(int matchId) {
        this.matchId = matchId;
    }

    public List<SkillRequest> getSkillrequests() {
        return skillrequests;
    }

    public void addSkillrequest(Skillrequest skillrequest) {
        this.skillrequests.add(skillrequest);
    }

}