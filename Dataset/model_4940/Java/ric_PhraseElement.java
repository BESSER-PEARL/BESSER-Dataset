





import java.util.List;
import java.util.ArrayList;

public class ric_PhraseElement extends InlineComponent, EventComponent, ClassifiableComponent, IdentifiableComponent {

    private String phraseType;
    private String title;



    public ric_PhraseElement(
        String phraseType,        String title    ) {
        super(
        );
        this.phraseType = phraseType;
        this.title = title;
    }


    public String getPhrasetype() {
        return phraseType;
    }

    public void setPhrasetype(String phraseType) {
        this.phraseType = phraseType;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}