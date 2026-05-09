





import java.util.List;
import java.util.ArrayList;

public class SMVC_View  {

    private String text;





    private List<SMVC_Component> smvc_components;


    public SMVC_View(
        String text    ) {
        this.text = text;
        this.smvc_components = new ArrayList<>();
    }

    public SMVC_View(
        String text        ArrayList<SMVC_Component> smvc_components    ) {
        this.text = text;
        this.smvc_components = smvc_components;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public List<SMVC_Component> getSmvc_components() {
        return smvc_components;
    }

    public void addSmvc_component(Smvc_component smvc_component) {
        this.smvc_components.add(smvc_component);
    }

}