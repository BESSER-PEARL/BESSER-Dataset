





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_VarRef extends VariableReference {






    private arduinoDSL_VariableDeclaration arduinodsl_variabledeclaration;




    private arduinoDSL_Cast arduinodsl_cast;




    private arduinoDSL_EObject arduinodsl_eobject;


    public arduinoDSL_VarRef(
    ) {
        super(
        );
    }



    public arduinoDSL_VariableDeclaration getArduinodsl_variabledeclaration() {
        return arduinodsl_variabledeclaration;
    }

    public void setArduinodsl_variabledeclaration(arduinoDSL_VariableDeclaration arduinodsl_variabledeclaration) {
        this.arduinodsl_variabledeclaration = arduinodsl_variabledeclaration;
    }
    public arduinoDSL_Cast getArduinodsl_cast() {
        return arduinodsl_cast;
    }

    public void setArduinodsl_cast(arduinoDSL_Cast arduinodsl_cast) {
        this.arduinodsl_cast = arduinodsl_cast;
    }
    public arduinoDSL_EObject getArduinodsl_eobject() {
        return arduinodsl_eobject;
    }

    public void setArduinodsl_eobject(arduinoDSL_EObject arduinodsl_eobject) {
        this.arduinodsl_eobject = arduinodsl_eobject;
    }

}