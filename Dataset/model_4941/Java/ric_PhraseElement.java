





import java.util.List;
import java.util.ArrayList;

public class ric_PhraseElement extends InlineComponent, IdentifiableComponent, EventComponent, ClassifiableComponent {

    private String phraseType;
    private String title;





    private ric_FormControl ric_formcontrol;


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

    public ric_FormControl getRic_formcontrol() {
        return ric_formcontrol;
    }

    public void setRic_formcontrol(ric_FormControl ric_formcontrol) {
        this.ric_formcontrol = ric_formcontrol;
    }

}