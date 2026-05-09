





import java.util.List;
import java.util.ArrayList;

public class rapidml_AuthenticationMethod  {






    private List<rapidml_SecurityScope> rapidml_securityscopes;




    private rapidml_HasSecurityValue rapidml_hassecurityvalue;




    private rapidml_SecurityScheme rapidml_securityscheme;


    public rapidml_AuthenticationMethod(
    ) {
        this.rapidml_securityscopes = new ArrayList<>();
    }

    public rapidml_AuthenticationMethod(
        ArrayList<rapidml_SecurityScope> rapidml_securityscopes    ) {
        this.rapidml_securityscopes = rapidml_securityscopes;
    }


    public List<rapidml_SecurityScope> getRapidml_securityscopes() {
        return rapidml_securityscopes;
    }

    public void addRapidml_securityscope(Rapidml_securityscope rapidml_securityscope) {
        this.rapidml_securityscopes.add(rapidml_securityscope);
    }
    public rapidml_HasSecurityValue getRapidml_hassecurityvalue() {
        return rapidml_hassecurityvalue;
    }

    public void setRapidml_hassecurityvalue(rapidml_HasSecurityValue rapidml_hassecurityvalue) {
        this.rapidml_hassecurityvalue = rapidml_hassecurityvalue;
    }
    public rapidml_SecurityScheme getRapidml_securityscheme() {
        return rapidml_securityscheme;
    }

    public void setRapidml_securityscheme(rapidml_SecurityScheme rapidml_securityscheme) {
        this.rapidml_securityscheme = rapidml_securityscheme;
    }

}