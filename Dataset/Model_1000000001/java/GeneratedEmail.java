




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class GeneratedEmail  {

    private String body;
    private String subject;
    private LocalDateTime created_at;
    private int id;
    private LocalDateTime sent_at;
    private boolean is_sent;





    private Contact contact;




    private User user;


    public GeneratedEmail(
        String body,        String subject,        LocalDateTime created_at,        int id,        LocalDateTime sent_at,        boolean is_sent    ) {
        this.body = body;
        this.subject = subject;
        this.created_at = created_at;
        this.id = id;
        this.sent_at = sent_at;
        this.is_sent = is_sent;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
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
    public LocalDateTime getSent_at() {
        return sent_at;
    }

    public void setSent_at(LocalDateTime sent_at) {
        this.sent_at = sent_at;
    }
    public boolean getIs_sent() {
        return is_sent;
    }

    public void setIs_sent(boolean is_sent) {
        this.is_sent = is_sent;
    }

    public Contact getContact() {
        return contact;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}