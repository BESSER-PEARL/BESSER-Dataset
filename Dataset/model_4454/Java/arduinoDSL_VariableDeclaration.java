





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_VariableDeclaration extends SimpleStatement {

    private String name;
    private String type;





    private arduinoDSL_EObject arduinodsl_eobject;


    public arduinoDSL_VariableDeclaration(
        String name,        String type    ) {
        super(
        );
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public arduinoDSL_EObject getArduinodsl_eobject() {
        return arduinodsl_eobject;
    }

    public void setArduinodsl_eobject(arduinoDSL_EObject arduinodsl_eobject) {
        this.arduinodsl_eobject = arduinodsl_eobject;
    }

}