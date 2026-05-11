





import java.util.List;
import java.util.ArrayList;

public class avm_cyber_CyberModel extends DomainModel_ {

    private String Locator;
    private String Type;
    private String Class;



    public avm_cyber_CyberModel(
        String Locator,        String Type,        String Class    ) {
        super(
        );
        this.Locator = Locator;
        this.Type = Type;
        this.Class = Class;
    }


    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getClass() {
        return Class;
    }

    public void setClass(String Class) {
        this.Class = Class;
    }


}