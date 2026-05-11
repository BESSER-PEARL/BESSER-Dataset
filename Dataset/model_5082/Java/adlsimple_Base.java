





import java.util.List;
import java.util.ArrayList;

public class adlsimple_Base  {






    private List<adlsimple_Component> adlsimple_components;


    public adlsimple_Base(
    ) {
        this.adlsimple_components = new ArrayList<>();
    }

    public adlsimple_Base(
        ArrayList<adlsimple_Component> adlsimple_components    ) {
        this.adlsimple_components = adlsimple_components;
    }


    public List<adlsimple_Component> getAdlsimple_components() {
        return adlsimple_components;
    }

    public void addAdlsimple_component(Adlsimple_component adlsimple_component) {
        this.adlsimple_components.add(adlsimple_component);
    }

}