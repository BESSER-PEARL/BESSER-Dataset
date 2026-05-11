





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_Pattern  {

    private String name;
    private int num;





    private esper2Maude_Event esper2maude_event;




    private esper2Maude_Window esper2maude_window;




    private esper2Maude_Model esper2maude_model;




    private esper2Maude_LastSelectEntry esper2maude_lastselectentry;




    private esper2Maude_FilterFrom esper2maude_filterfrom;




    private List<esper2Maude_NonLastSelectEntry> esper2maude_nonlastselectentrys;


    public esper2Maude_Pattern(
        String name,        int num    ) {
        this.name = name;
        this.num = num;
        this.esper2maude_nonlastselectentrys = new ArrayList<>();
    }

    public esper2Maude_Pattern(
        String name,        int num        ArrayList<esper2Maude_NonLastSelectEntry> esper2maude_nonlastselectentrys    ) {
        this.name = name;
        this.num = num;
        this.esper2maude_nonlastselectentrys = esper2maude_nonlastselectentrys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public esper2Maude_Event getEsper2maude_event() {
        return esper2maude_event;
    }

    public void setEsper2maude_event(esper2Maude_Event esper2maude_event) {
        this.esper2maude_event = esper2maude_event;
    }
    public esper2Maude_Window getEsper2maude_window() {
        return esper2maude_window;
    }

    public void setEsper2maude_window(esper2Maude_Window esper2maude_window) {
        this.esper2maude_window = esper2maude_window;
    }
    public esper2Maude_Model getEsper2maude_model() {
        return esper2maude_model;
    }

    public void setEsper2maude_model(esper2Maude_Model esper2maude_model) {
        this.esper2maude_model = esper2maude_model;
    }
    public esper2Maude_LastSelectEntry getEsper2maude_lastselectentry() {
        return esper2maude_lastselectentry;
    }

    public void setEsper2maude_lastselectentry(esper2Maude_LastSelectEntry esper2maude_lastselectentry) {
        this.esper2maude_lastselectentry = esper2maude_lastselectentry;
    }
    public esper2Maude_FilterFrom getEsper2maude_filterfrom() {
        return esper2maude_filterfrom;
    }

    public void setEsper2maude_filterfrom(esper2Maude_FilterFrom esper2maude_filterfrom) {
        this.esper2maude_filterfrom = esper2maude_filterfrom;
    }
    public List<esper2Maude_NonLastSelectEntry> getEsper2maude_nonlastselectentrys() {
        return esper2maude_nonlastselectentrys;
    }

    public void addEsper2maude_nonlastselectentry(Esper2maude_nonlastselectentry esper2maude_nonlastselectentry) {
        this.esper2maude_nonlastselectentrys.add(esper2maude_nonlastselectentry);
    }

}