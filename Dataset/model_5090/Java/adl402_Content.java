





import java.util.List;
import java.util.ArrayList;

public class adl402_Content  {

    private String language;
    private String expression;





    private adl402_Component adl402_component;




    private List<adl402_EClass0> adl402_eclass0s;




    private adl402_Component adl402_component;


    public adl402_Content(
        String language,        String expression    ) {
        this.language = language;
        this.expression = expression;
        this.adl402_eclass0s = new ArrayList<>();
    }

    public adl402_Content(
        String language,        String expression        ArrayList<adl402_EClass0> adl402_eclass0s    ) {
        this.language = language;
        this.expression = expression;
        this.adl402_eclass0s = adl402_eclass0s;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public adl402_Component getAdl402_component() {
        return adl402_component;
    }

    public void setAdl402_component(adl402_Component adl402_component) {
        this.adl402_component = adl402_component;
    }
    public List<adl402_EClass0> getAdl402_eclass0s() {
        return adl402_eclass0s;
    }

    public void addAdl402_eclass0(Adl402_eclass0 adl402_eclass0) {
        this.adl402_eclass0s.add(adl402_eclass0);
    }
    public adl402_Component getAdl402_component() {
        return adl402_component;
    }

    public void setAdl402_component(adl402_Component adl402_component) {
        this.adl402_component = adl402_component;
    }

}