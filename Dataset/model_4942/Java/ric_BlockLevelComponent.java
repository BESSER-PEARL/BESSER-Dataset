





import java.util.List;
import java.util.ArrayList;

public class ric_BlockLevelComponent  {






    private List<ric_BlockLevelComponent> ric_blocklevelcomponents;




    private ric_Form ric_form;




    private ric_Document ric_document;


    public ric_BlockLevelComponent(
    ) {
        this.ric_blocklevelcomponents = new ArrayList<>();
    }

    public ric_BlockLevelComponent(
        ArrayList<ric_BlockLevelComponent> ric_blocklevelcomponents    ) {
        this.ric_blocklevelcomponents = ric_blocklevelcomponents;
    }


    public List<ric_BlockLevelComponent> getRic_blocklevelcomponents() {
        return ric_blocklevelcomponents;
    }

    public void addRic_blocklevelcomponent(Ric_blocklevelcomponent ric_blocklevelcomponent) {
        this.ric_blocklevelcomponents.add(ric_blocklevelcomponent);
    }
    public ric_Form getRic_form() {
        return ric_form;
    }

    public void setRic_form(ric_Form ric_form) {
        this.ric_form = ric_form;
    }
    public ric_Document getRic_document() {
        return ric_document;
    }

    public void setRic_document(ric_Document ric_document) {
        this.ric_document = ric_document;
    }

}