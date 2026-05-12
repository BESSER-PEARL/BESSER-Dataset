





import java.util.List;
import java.util.ArrayList;

public class conference_Subject  {

    private String description;
    private boolean isDone;





    private conference_Talk conference_talk;


    public conference_Subject(
        String description,        boolean isDone    ) {
        this.description = description;
        this.isDone = isDone;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getIsdone() {
        return isDone;
    }

    public void setIsdone(boolean isDone) {
        this.isDone = isDone;
    }

    public conference_Talk getConference_talk() {
        return conference_talk;
    }

    public void setConference_talk(conference_Talk conference_talk) {
        this.conference_talk = conference_talk;
    }

}