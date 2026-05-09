





import java.util.List;
import java.util.ArrayList;

public class eol_module_NameExpression extends Expression {

    private boolean isType;
    private String name;





    private eol_module_OperationDefinition eol_module_operationdefinition;


    public eol_module_NameExpression(
        boolean isType,        String name    ) {
        super(
        );
        this.isType = isType;
        this.name = name;
    }


    public boolean getIstype() {
        return isType;
    }

    public void setIstype(boolean isType) {
        this.isType = isType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eol_module_OperationDefinition getEol_module_operationdefinition() {
        return eol_module_operationdefinition;
    }

    public void setEol_module_operationdefinition(eol_module_OperationDefinition eol_module_operationdefinition) {
        this.eol_module_operationdefinition = eol_module_operationdefinition;
    }

}