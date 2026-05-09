





import java.util.List;
import java.util.ArrayList;

public class rapidml_SecuritySchemeParameter extends Documentable {

    private String value;
    private String name;





    private rapidml_SecurityScheme rapidml_securityscheme;


    public rapidml_SecuritySchemeParameter(
        String value,        String name    ) {
        super(
        );
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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