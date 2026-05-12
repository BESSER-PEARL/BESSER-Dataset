





import java.util.List;
import java.util.ArrayList;

public class documentation_TextContainer  {






    private List<documentation_Text> documentation_texts;


    public documentation_TextContainer(
    ) {
        this.documentation_texts = new ArrayList<>();
    }

    public documentation_TextContainer(
        ArrayList<documentation_Text> documentation_texts    ) {
        this.documentation_texts = documentation_texts;
    }


    public List<documentation_Text> getDocumentation_texts() {
        return documentation_texts;
    }

    public void addDocumentation_text(Documentation_text documentation_text) {
        this.documentation_texts.add(documentation_text);
    }

}