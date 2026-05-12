





import java.util.List;
import java.util.ArrayList;

public class conference_Topic  {

    private String documentation;
    private String description;
    private String references;





    private conference_Talk conference_talk;


    public conference_Topic(
        String documentation,        String description,        String references    ) {
        this.documentation = documentation;
        this.description = description;
        this.references = references;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getReferences() {
        return references;
    }

    public void setReferences(String references) {
        this.references = references;
    }

    public conference_Talk getConference_talk() {
        return conference_talk;
    }

    public void setConference_talk(conference_Talk conference_talk) {
        this.conference_talk = conference_talk;
    }

}