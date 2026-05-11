





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Parameter  {

    private String name;





    private kmLogo_ParameterCall kmlogo_parametercall;




    private kmLogo_ProcDeclaration kmlogo_procdeclaration;


    public kmLogo_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public kmLogo_ParameterCall getKmlogo_parametercall() {
        return kmlogo_parametercall;
    }

    public void setKmlogo_parametercall(kmLogo_ParameterCall kmlogo_parametercall) {
        this.kmlogo_parametercall = kmlogo_parametercall;
    }
    public kmLogo_ProcDeclaration getKmlogo_procdeclaration() {
        return kmlogo_procdeclaration;
    }

    public void setKmlogo_procdeclaration(kmLogo_ProcDeclaration kmlogo_procdeclaration) {
        this.kmlogo_procdeclaration = kmlogo_procdeclaration;
    }

}