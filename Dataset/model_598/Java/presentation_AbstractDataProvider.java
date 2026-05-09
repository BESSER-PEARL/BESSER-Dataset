





import java.util.List;
import java.util.ArrayList;

public class presentation_AbstractDataProvider  {

    private String group;
    private String key;
    private String mixed;





    private List<presentation_IBindingContext> presentation_ibindingcontexts;


    public presentation_AbstractDataProvider(
        String group,        String key,        String mixed    ) {
        this.group = group;
        this.key = key;
        this.mixed = mixed;
        this.presentation_ibindingcontexts = new ArrayList<>();
    }

    public presentation_AbstractDataProvider(
        String group,        String key,        String mixed        ArrayList<presentation_IBindingContext> presentation_ibindingcontexts    ) {
        this.group = group;
        this.key = key;
        this.mixed = mixed;
        this.presentation_ibindingcontexts = presentation_ibindingcontexts;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<presentation_IBindingContext> getPresentation_ibindingcontexts() {
        return presentation_ibindingcontexts;
    }

    public void addPresentation_ibindingcontext(Presentation_ibindingcontext presentation_ibindingcontext) {
        this.presentation_ibindingcontexts.add(presentation_ibindingcontext);
    }

}