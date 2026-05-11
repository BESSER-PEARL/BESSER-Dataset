





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Alternative  {

    private String description;





    private jpdl31_Question jpdl31_question;


    public jpdl31_Alternative(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public jpdl31_Question getJpdl31_question() {
        return jpdl31_question;
    }

    public void setJpdl31_question(jpdl31_Question jpdl31_question) {
        this.jpdl31_question = jpdl31_question;
    }

}