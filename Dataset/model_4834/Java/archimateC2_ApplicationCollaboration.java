





import java.util.List;
import java.util.ArrayList;

public class archimateC2_ApplicationCollaboration extends ApplicationComponent {






    private archimateC2_ApplicationComponent archimatec2_applicationcomponent;




    private List<archimateC2_ApplicationComponent> archimatec2_applicationcomponents;


    public archimateC2_ApplicationCollaboration(
    ) {
        super(
        );
        this.archimatec2_applicationcomponents = new ArrayList<>();
    }

    public archimateC2_ApplicationCollaboration(
        ArrayList<archimateC2_ApplicationComponent> archimatec2_applicationcomponents    ) {
        this.archimatec2_applicationcomponents = archimatec2_applicationcomponents;
    }


    public archimateC2_ApplicationComponent getArchimatec2_applicationcomponent() {
        return archimatec2_applicationcomponent;
    }

    public void setArchimatec2_applicationcomponent(archimateC2_ApplicationComponent archimatec2_applicationcomponent) {
        this.archimatec2_applicationcomponent = archimatec2_applicationcomponent;
    }
    public List<archimateC2_ApplicationComponent> getArchimatec2_applicationcomponents() {
        return archimatec2_applicationcomponents;
    }

    public void addArchimatec2_applicationcomponent(Archimatec2_applicationcomponent archimatec2_applicationcomponent) {
        this.archimatec2_applicationcomponents.add(archimatec2_applicationcomponent);
    }

}