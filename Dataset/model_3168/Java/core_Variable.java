





import java.util.List;
import java.util.ArrayList;

public class core_Variable  {

    private String name;





    private core_PropertyWrite core_propertywrite;




    private core_VariableReference core_variablereference;


    public core_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public core_PropertyWrite getCore_propertywrite() {
        return core_propertywrite;
    }

    public void setCore_propertywrite(core_PropertyWrite core_propertywrite) {
        this.core_propertywrite = core_propertywrite;
    }
    public core_VariableReference getCore_variablereference() {
        return core_variablereference;
    }

    public void setCore_variablereference(core_VariableReference core_variablereference) {
        this.core_variablereference = core_variablereference;
    }

}