





import java.util.List;
import java.util.ArrayList;

public class urml_UrmlModelElement extends UnicaseModelElement {

    private boolean reviewed;





    private List<urml_UrmlModelElement> urml_urmlmodelelements;


    public urml_UrmlModelElement(
        boolean reviewed    ) {
        super(
        );
        this.reviewed = reviewed;
        this.urml_urmlmodelelements = new ArrayList<>();
    }

    public urml_UrmlModelElement(
        boolean reviewed        ArrayList<urml_UrmlModelElement> urml_urmlmodelelements    ) {
        this.reviewed = reviewed;
        this.urml_urmlmodelelements = urml_urmlmodelelements;
    }

    public boolean getReviewed() {
        return reviewed;
    }

    public void setReviewed(boolean reviewed) {
        this.reviewed = reviewed;
    }

    public List<urml_UrmlModelElement> getUrml_urmlmodelelements() {
        return urml_urmlmodelelements;
    }

    public void addUrml_urmlmodelelement(Urml_urmlmodelelement urml_urmlmodelelement) {
        this.urml_urmlmodelelements.add(urml_urmlmodelelement);
    }

}