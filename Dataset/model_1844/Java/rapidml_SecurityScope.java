





import java.util.List;
import java.util.ArrayList;

public class rapidml_SecurityScope extends Documentable {

    private String name;





    private rapidml_SecurityScheme rapidml_securityscheme;


    public rapidml_SecurityScope(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rapidml_SecurityScheme getRapidml_securityscheme() {
        return rapidml_securityscheme;
    }

    public void setRapidml_securityscheme(rapidml_SecurityScheme rapidml_securityscheme) {
        this.rapidml_securityscheme = rapidml_securityscheme;
    }

}