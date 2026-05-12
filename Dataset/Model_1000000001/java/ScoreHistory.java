




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class ScoreHistory  {

    private int new_score;
    private int old_score;
    private int id;
    private LocalDateTime calculated_at;
    private String reason;





    private Contact contact;


    public ScoreHistory(
        int new_score,        int old_score,        int id,        LocalDateTime calculated_at,        String reason    ) {
        this.new_score = new_score;
        this.old_score = old_score;
        this.id = id;
        this.calculated_at = calculated_at;
        this.reason = reason;
    }


    public int getNew_score() {
        return new_score;
    }

    public void setNew_score(int new_score) {
        this.new_score = new_score;
    }
    public int getOld_score() {
        return old_score;
    }

    public void setOld_score(int old_score) {
        this.old_score = old_score;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDateTime getCalculated_at() {
        return calculated_at;
    }

    public void setCalculated_at(LocalDateTime calculated_at) {
        this.calculated_at = calculated_at;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }

    public Contact getContact() {
        return contact;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }

}