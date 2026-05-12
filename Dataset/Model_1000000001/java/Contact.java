




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class Contact  {

    private boolean is_enriched;
    private LocalDateTime updated_at;
    private String last_name;
    private String phone;
    private String profile_picture_url;
    private None lead_score_level;
    private String notes;
    private String first_name;
    private String job_title;
    private String email;
    private LocalDateTime created_at;
    private int id;
    private int lead_score;
    private String linkedin_url;





    private List<Opportunity> opportunitys;


    public Contact(
        boolean is_enriched,        LocalDateTime updated_at,        String last_name,        String phone,        String profile_picture_url,        None lead_score_level,        String notes,        String first_name,        String job_title,        String email,        LocalDateTime created_at,        int id,        int lead_score,        String linkedin_url    ) {
        this.is_enriched = is_enriched;
        this.updated_at = updated_at;
        this.last_name = last_name;
        this.phone = phone;
        this.profile_picture_url = profile_picture_url;
        this.lead_score_level = lead_score_level;
        this.notes = notes;
        this.first_name = first_name;
        this.job_title = job_title;
        this.email = email;
        this.created_at = created_at;
        this.id = id;
        this.lead_score = lead_score;
        this.linkedin_url = linkedin_url;
        this.opportunitys = new ArrayList<>();
    }

    public Contact(
        boolean is_enriched,        LocalDateTime updated_at,        String last_name,        String phone,        String profile_picture_url,        None lead_score_level,        String notes,        String first_name,        String job_title,        String email,        LocalDateTime created_at,        int id,        int lead_score,        String linkedin_url        ArrayList<Opportunity> opportunitys    ) {
        this.is_enriched = is_enriched;
        this.updated_at = updated_at;
        this.last_name = last_name;
        this.phone = phone;
        this.profile_picture_url = profile_picture_url;
        this.lead_score_level = lead_score_level;
        this.notes = notes;
        this.first_name = first_name;
        this.job_title = job_title;
        this.email = email;
        this.created_at = created_at;
        this.id = id;
        this.lead_score = lead_score;
        this.linkedin_url = linkedin_url;
        this.opportunitys = opportunitys;
    }

    public boolean getIs_enriched() {
        return is_enriched;
    }

    public void setIs_enriched(boolean is_enriched) {
        this.is_enriched = is_enriched;
    }
    public LocalDateTime getUpdated_at() {
        return updated_at;
    }

    public void setUpdated_at(LocalDateTime updated_at) {
        this.updated_at = updated_at;
    }
    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getProfile_picture_url() {
        return profile_picture_url;
    }

    public void setProfile_picture_url(String profile_picture_url) {
        this.profile_picture_url = profile_picture_url;
    }
    public None getLead_score_level() {
        return lead_score_level;
    }

    public void setLead_score_level(None lead_score_level) {
        this.lead_score_level = lead_score_level;
    }
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public String getJob_title() {
        return job_title;
    }

    public void setJob_title(String job_title) {
        this.job_title = job_title;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public LocalDateTime getCreated_at() {
        return created_at;
    }

    public void setCreated_at(LocalDateTime created_at) {
        this.created_at = created_at;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getLead_score() {
        return lead_score;
    }

    public void setLead_score(int lead_score) {
        this.lead_score = lead_score;
    }
    public String getLinkedin_url() {
        return linkedin_url;
    }

    public void setLinkedin_url(String linkedin_url) {
        this.linkedin_url = linkedin_url;
    }

    public List<Opportunity> getOpportunitys() {
        return opportunitys;
    }

    public void addOpportunity(Opportunity opportunity) {
        this.opportunitys.add(opportunity);
    }

}