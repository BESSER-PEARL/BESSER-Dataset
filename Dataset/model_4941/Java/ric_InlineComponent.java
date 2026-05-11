





import java.util.List;
import java.util.ArrayList;

public class ric_InlineComponent  {

    private String text;





    private ric_Document ric_document;




    private List<ric_InlineComponent> ric_inlinecomponents;




    private ric_Form ric_form;




    private ric_BlockLevelComponent ric_blocklevelcomponent;


    public ric_InlineComponent(
        String text    ) {
        this.text = text;
        this.ric_inlinecomponents = new ArrayList<>();
    }

    public ric_InlineComponent(
        String text        ArrayList<ric_InlineComponent> ric_inlinecomponents    ) {
        this.text = text;
        this.ric_inlinecomponents = ric_inlinecomponents;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public ric_Document getRic_document() {
        return ric_document;
    }

    public void setRic_document(ric_Document ric_document) {
        this.ric_document = ric_document;
    }
    public List<ric_InlineComponent> getRic_inlinecomponents() {
        return ric_inlinecomponents;
    }

    public void addRic_inlinecomponent(Ric_inlinecomponent ric_inlinecomponent) {
        this.ric_inlinecomponents.add(ric_inlinecomponent);
    }
    public ric_Form getRic_form() {
        return ric_form;
    }

    public void setRic_form(ric_Form ric_form) {
        this.ric_form = ric_form;
    }
    public ric_BlockLevelComponent getRic_blocklevelcomponent() {
        return ric_blocklevelcomponent;
    }

    public void setRic_blocklevelcomponent(ric_BlockLevelComponent ric_blocklevelcomponent) {
        this.ric_blocklevelcomponent = ric_blocklevelcomponent;
    }

}