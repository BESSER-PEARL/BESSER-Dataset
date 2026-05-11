





import java.util.List;
import java.util.ArrayList;

public class logo_Parameter  {

    private String name;





    private logo_ParameterCall logo_parametercall;




    private logo_ProcDeclaration logo_procdeclaration;


    public logo_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public logo_ParameterCall getLogo_parametercall() {
        return logo_parametercall;
    }

    public void setLogo_parametercall(logo_ParameterCall logo_parametercall) {
        this.logo_parametercall = logo_parametercall;
    }
    public logo_ProcDeclaration getLogo_procdeclaration() {
        return logo_procdeclaration;
    }

    public void setLogo_procdeclaration(logo_ProcDeclaration logo_procdeclaration) {
        this.logo_procdeclaration = logo_procdeclaration;
    }

}