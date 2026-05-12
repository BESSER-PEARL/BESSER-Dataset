




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class SkillRequest  {

    private LocalDate deadlineDate;
    private int requestId;
    private LocalDate createdDate;
    private None status;





    private Skill skill;




    private User user;


    public SkillRequest(
        LocalDate deadlineDate,        int requestId,        LocalDate createdDate,        None status    ) {
        this.deadlineDate = deadlineDate;
        this.requestId = requestId;
        this.createdDate = createdDate;
        this.status = status;
    }


    public LocalDate getDeadlinedate() {
        return deadlineDate;
    }

    public void setDeadlinedate(LocalDate deadlineDate) {
        this.deadlineDate = deadlineDate;
    }
    public int getRequestid() {
        return requestId;
    }

    public void setRequestid(int requestId) {
        this.requestId = requestId;
    }
    public LocalDate getCreateddate() {
        return createdDate;
    }

    public void setCreateddate(LocalDate createdDate) {
        this.createdDate = createdDate;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }

    public Skill getSkill() {
        return skill;
    }

    public void setSkill(Skill skill) {
        this.skill = skill;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}