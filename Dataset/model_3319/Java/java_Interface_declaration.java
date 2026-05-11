





import java.util.List;
import java.util.ArrayList;

public class java_Interface_declaration  {

    private String extend;
    private String extends;
    private String interfaceName;
    private String modifiers;



    public java_Interface_declaration(
        String extend,        String extends,        String interfaceName,        String modifiers    ) {
        this.extend = extend;
        this.extends = extends;
        this.interfaceName = interfaceName;
        this.modifiers = modifiers;
    }


    public String getExtend() {
        return extend;
    }

    public void setExtend(String extend) {
        this.extend = extend;
    }
    public String getExtends() {
        return extends;
    }

    public void setExtends(String extends) {
        this.extends = extends;
    }
    public String getInterfacename() {
        return interfaceName;
    }

    public void setInterfacename(String interfaceName) {
        this.interfaceName = interfaceName;
    }
    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }


}