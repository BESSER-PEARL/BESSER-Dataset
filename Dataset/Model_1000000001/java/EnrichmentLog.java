




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class EnrichmentLog  {

    private String linkedin_url;
    private LocalDateTime enriched_at;
    private int id;
    private String error_message;
    private boolean is_successful;





    private Contact contact;


    public EnrichmentLog(
        String linkedin_url,        LocalDateTime enriched_at,        int id,        String error_message,        boolean is_successful    ) {
        this.linkedin_url = linkedin_url;
        this.enriched_at = enriched_at;
        this.id = id;
        this.error_message = error_message;
        this.is_successful = is_successful;
    }


    public String getLinkedin_url() {
        return linkedin_url;
    }

    public void setLinkedin_url(String linkedin_url) {
        this.linkedin_url = linkedin_url;
    }
    public LocalDateTime getEnriched_at() {
        return enriched_at;
    }

    public void setEnriched_at(LocalDateTime enriched_at) {
        this.enriched_at = enriched_at;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getError_message() {
        return error_message;
    }

    public void setError_message(String error_message) {
        this.error_message = error_message;
    }
    public boolean getIs_successful() {
        return is_successful;
    }

    public void setIs_successful(boolean is_successful) {
        this.is_successful = is_successful;
    }

    public Contact getContact() {
        return contact;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }

}