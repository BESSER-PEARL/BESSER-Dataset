





import java.util.List;
import java.util.ArrayList;

public class Question  {

    private String definition;
    private String explanation;





    private Section section;


    public Question(
        String definition,        String explanation    ) {
        this.definition = definition;
        this.explanation = explanation;
    }


    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    public String getExplanation() {
        return explanation;
    }

    public void setExplanation(String explanation) {
        this.explanation = explanation;
    }

    public Section getSection() {
        return section;
    }

    public void setSection(Section section) {
        this.section = section;
    }

}