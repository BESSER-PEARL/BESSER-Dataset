





import java.util.List;
import java.util.ArrayList;

public class adl101_Component  {

    private String name;





    private adl101_Component adl101_component;




    private adl101_Content adl101_content;




    private List<adl101_Provided> adl101_provideds;




    private adl101_Content adl101_content;


    public adl101_Component(
        String name    ) {
        this.name = name;
        this.adl101_provideds = new ArrayList<>();
    }

    public adl101_Component(
        String name        ArrayList<adl101_Provided> adl101_provideds    ) {
        this.name = name;
        this.adl101_provideds = adl101_provideds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adl101_Component getAdl101_component() {
        return adl101_component;
    }

    public void setAdl101_component(adl101_Component adl101_component) {
        this.adl101_component = adl101_component;
    }
    public adl101_Content getAdl101_content() {
        return adl101_content;
    }

    public void setAdl101_content(adl101_Content adl101_content) {
        this.adl101_content = adl101_content;
    }
    public List<adl101_Provided> getAdl101_provideds() {
        return adl101_provideds;
    }

    public void addAdl101_provided(Adl101_provided adl101_provided) {
        this.adl101_provideds.add(adl101_provided);
    }
    public adl101_Content getAdl101_content() {
        return adl101_content;
    }

    public void setAdl101_content(adl101_Content adl101_content) {
        this.adl101_content = adl101_content;
    }

}