





import java.util.List;
import java.util.ArrayList;

public class avm_cyber_CyberModel extends DomainModel_ {

    private String Type;
    private String Class;
    private String Locator;



    public avm_cyber_CyberModel(
        String Type,        String Class,        String Locator    ) {
        super(
        );
        this.Type = Type;
        this.Class = Class;
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
    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }


}