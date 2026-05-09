





import java.util.List;
import java.util.ArrayList;

public class rapidml_SecuritySchemeLibrary extends Documentable {

    private String name;





    private List<rapidml_SecurityScheme> rapidml_securityschemes;




    private rapidml_ZenModel rapidml_zenmodel;


    public rapidml_SecuritySchemeLibrary(
        String name    ) {
        super(
        );
        this.name = name;
        this.rapidml_securityschemes = new ArrayList<>();
    }

    public rapidml_SecuritySchemeLibrary(
        String name        ArrayList<rapidml_SecurityScheme> rapidml_securityschemes    ) {
        this.name = name;
        this.rapidml_securityschemes = rapidml_securityschemes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<rapidml_SecurityScheme> getRapidml_securityschemes() {
        return rapidml_securityschemes;
    }

    public void addRapidml_securityscheme(Rapidml_securityscheme rapidml_securityscheme) {
        this.rapidml_securityschemes.add(rapidml_securityscheme);
    }
    public rapidml_ZenModel getRapidml_zenmodel() {
        return rapidml_zenmodel;
    }

    public void setRapidml_zenmodel(rapidml_ZenModel rapidml_zenmodel) {
        this.rapidml_zenmodel = rapidml_zenmodel;
    }

}