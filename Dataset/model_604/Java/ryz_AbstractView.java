





import java.util.List;
import java.util.ArrayList;

public class ryz_AbstractView extends MainComponent {






    private List<ryz_PresentationElement> ryz_presentationelements;




    private ryz_ViewPackage ryz_viewpackage;


    public ryz_AbstractView(
    ) {
        super(
        );
        this.ryz_presentationelements = new ArrayList<>();
    }

    public ryz_AbstractView(
        ArrayList<ryz_PresentationElement> ryz_presentationelements    ) {
        this.ryz_presentationelements = ryz_presentationelements;
    }


    public List<ryz_PresentationElement> getRyz_presentationelements() {
        return ryz_presentationelements;
    }

    public void addRyz_presentationelement(Ryz_presentationelement ryz_presentationelement) {
        this.ryz_presentationelements.add(ryz_presentationelement);
    }
    public ryz_ViewPackage getRyz_viewpackage() {
        return ryz_viewpackage;
    }

    public void setRyz_viewpackage(ryz_ViewPackage ryz_viewpackage) {
        this.ryz_viewpackage = ryz_viewpackage;
    }

}