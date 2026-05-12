




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class EmailTemplate  {

    private String body_template;
    private String subject_template;
    private int id;
    private String name;
    private LocalDateTime created_at;
    private String category;





    private List<GeneratedEmail> generatedemails;




    private User user;


    public EmailTemplate(
        String body_template,        String subject_template,        int id,        String name,        LocalDateTime created_at,        String category    ) {
        this.body_template = body_template;
        this.subject_template = subject_template;
        this.id = id;
        this.name = name;
        this.created_at = created_at;
        this.category = category;
        this.generatedemails = new ArrayList<>();
    }

    public EmailTemplate(
        String body_template,        String subject_template,        int id,        String name,        LocalDateTime created_at,        String category        ArrayList<GeneratedEmail> generatedemails    ) {
        this.body_template = body_template;
        this.subject_template = subject_template;
        this.id = id;
        this.name = name;
        this.created_at = created_at;
        this.category = category;
        this.generatedemails = generatedemails;
    }

    public String getBody_template() {
        return body_template;
    }

    public void setBody_template(String body_template) {
        this.body_template = body_template;
    }
    public String getSubject_template() {
        return subject_template;
    }

    public void setSubject_template(String subject_template) {
        this.subject_template = subject_template;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDateTime getCreated_at() {
        return created_at;
    }

    public void setCreated_at(LocalDateTime created_at) {
        this.created_at = created_at;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public List<GeneratedEmail> getGeneratedemails() {
        return generatedemails;
    }

    public void addGeneratedemail(Generatedemail generatedemail) {
        this.generatedemails.add(generatedemail);
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}