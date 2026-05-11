





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Parameter  {

    private String name;





    private kmLogo_ParameterCall kmlogo_parametercall;




    private kmLogo_MethodeDeclaration kmlogo_methodedeclaration;


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
    public kmLogo_MethodeDeclaration getKmlogo_methodedeclaration() {
        return kmlogo_methodedeclaration;
    }

    public void setKmlogo_methodedeclaration(kmLogo_MethodeDeclaration kmlogo_methodedeclaration) {
        this.kmlogo_methodedeclaration = kmlogo_methodedeclaration;
    }

}