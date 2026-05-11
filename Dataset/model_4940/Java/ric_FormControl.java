





import java.util.List;
import java.util.ArrayList;

public class ric_FormControl extends EventComponent, ClassifiableComponent, IdentifiableComponent {

    private String value;
    private String name;





    private ric_Label ric_label;




    private List<ric_PhraseElement> ric_phraseelements;




    private ric_Fieldset ric_fieldset;


    public ric_FormControl(
        String value,        String name    ) {
        super(
        );
        this.value = value;
        this.name = name;
        this.ric_phraseelements = new ArrayList<>();
    }

    public ric_FormControl(
        String value,        String name        ArrayList<ric_PhraseElement> ric_phraseelements    ) {
        this.value = value;
        this.name = name;
        this.ric_phraseelements = ric_phraseelements;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ric_Label getRic_label() {
        return ric_label;
    }

    public void setRic_label(ric_Label ric_label) {
        this.ric_label = ric_label;
    }
    public List<ric_PhraseElement> getRic_phraseelements() {
        return ric_phraseelements;
    }

    public void addRic_phraseelement(Ric_phraseelement ric_phraseelement) {
        this.ric_phraseelements.add(ric_phraseelement);
    }
    public ric_Fieldset getRic_fieldset() {
        return ric_fieldset;
    }

    public void setRic_fieldset(ric_Fieldset ric_fieldset) {
        this.ric_fieldset = ric_fieldset;
    }

}