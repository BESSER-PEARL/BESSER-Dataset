





import java.util.List;
import java.util.ArrayList;

public class dsml_web_Form  {

    private String action;





    private List<FormElement> formelements;


    public dsml_web_Form(
        String action    ) {
        this.action = action;
        this.formelements = new ArrayList<>();
    }

    public dsml_web_Form(
        String action        ArrayList<FormElement> formelements    ) {
        this.action = action;
        this.formelements = formelements;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public List<FormElement> getFormelements() {
        return formelements;
    }

    public void addFormelement(Formelement formelement) {
        this.formelements.add(formelement);
    }

}