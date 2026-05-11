





import java.util.List;
import java.util.ArrayList;

public class geoff_GeoMap extends Identifiable, Descriptive {

    private String rendererHint;





    private List<Layer> layers;




    private List<Interaction> interactions;




    private geoff_View geoff_view;




    private List<geoff_Script> geoff_scripts;


    public geoff_GeoMap(
        String rendererHint    ) {
        super(
        );
        this.rendererHint = rendererHint;
        this.layers = new ArrayList<>();
        this.interactions = new ArrayList<>();
        this.geoff_scripts = new ArrayList<>();
    }

    public geoff_GeoMap(
        String rendererHint        ArrayList<Layer> layers,        ArrayList<Interaction> interactions,        ArrayList<geoff_Script> geoff_scripts    ) {
        this.rendererHint = rendererHint;
        this.layers = layers;
        this.interactions = interactions;
        this.geoff_scripts = geoff_scripts;
    }

    public String getRendererhint() {
        return rendererHint;
    }

    public void setRendererhint(String rendererHint) {
        this.rendererHint = rendererHint;
    }

    public List<Layer> getLayers() {
        return layers;
    }

    public void addLayer(Layer layer) {
        this.layers.add(layer);
    }
    public List<Interaction> getInteractions() {
        return interactions;
    }

    public void addInteraction(Interaction interaction) {
        this.interactions.add(interaction);
    }
    public geoff_View getGeoff_view() {
        return geoff_view;
    }

    public void setGeoff_view(geoff_View geoff_view) {
        this.geoff_view = geoff_view;
    }
    public List<geoff_Script> getGeoff_scripts() {
        return geoff_scripts;
    }

    public void addGeoff_script(Geoff_script geoff_script) {
        this.geoff_scripts.add(geoff_script);
    }

}