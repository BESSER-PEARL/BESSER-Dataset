




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Session  {

    private LocalDate sessionDate;
    private int sessionId;
    private None sessionType;
    private int duration;





    private SkillMatch skillmatch;




    private Review review;


    public Session(
        LocalDate sessionDate,        int sessionId,        None sessionType,        int duration    ) {
        this.sessionDate = sessionDate;
        this.sessionId = sessionId;
        this.sessionType = sessionType;
        this.duration = duration;
    }


    public LocalDate getSessiondate() {
        return sessionDate;
    }

    public void setSessiondate(LocalDate sessionDate) {
        this.sessionDate = sessionDate;
    }
    public int getSessionid() {
        return sessionId;
    }

    public void setSessionid(int sessionId) {
        this.sessionId = sessionId;
    }
    public None getSessiontype() {
        return sessionType;
    }

    public void setSessiontype(None sessionType) {
        this.sessionType = sessionType;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    public SkillMatch getSkillmatch() {
        return skillmatch;
    }

    public void setSkillmatch(SkillMatch skillmatch) {
        this.skillmatch = skillmatch;
    }
    public Review getReview() {
        return review;
    }

    public void setReview(Review review) {
        this.review = review;
    }

}