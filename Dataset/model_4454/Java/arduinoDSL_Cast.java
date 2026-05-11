





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_Cast  {

    private String castType;





    private arduinoDSL_VariableDeclaration arduinodsl_variabledeclaration;


    public arduinoDSL_Cast(
        String castType    ) {
        this.castType = castType;
    }


    public String getCasttype() {
        return castType;
    }

    public void setCasttype(String castType) {
        this.castType = castType;
    }

    public arduinoDSL_VariableDeclaration getArduinodsl_variabledeclaration() {
        return arduinodsl_variabledeclaration;
    }

    public void setArduinodsl_variabledeclaration(arduinoDSL_VariableDeclaration arduinodsl_variabledeclaration) {
        this.arduinodsl_variabledeclaration = arduinodsl_variabledeclaration;
    }

}