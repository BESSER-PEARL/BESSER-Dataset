




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class Interaction  {

    private None type;
    private String content;
    private LocalDateTime occurred_at;
    private LocalDateTime created_at;
    private int id;
    private String subject;
    private None direction;





    private User user;




    private Contact contact;


    public Interaction(
        None type,        String content,        LocalDateTime occurred_at,        LocalDateTime created_at,        int id,        String subject,        None direction    ) {
        this.type = type;
        this.content = content;
        this.occurred_at = occurred_at;
        this.created_at = created_at;
        this.id = id;
        this.subject = subject;
        this.direction = direction;
    }


    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public LocalDateTime getOccurred_at() {
        return occurred_at;
    }

    public void setOccurred_at(LocalDateTime occurred_at) {
        this.occurred_at = occurred_at;
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
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public None getDirection() {
        return direction;
    }

    public void setDirection(None direction) {
        this.direction = direction;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Contact getContact() {
        return contact;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }

}