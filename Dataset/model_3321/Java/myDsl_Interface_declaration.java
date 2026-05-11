





import java.util.List;
import java.util.ArrayList;

public class myDsl_Interface_declaration  {

    private String interfaceHerdada;
    private String modifiers;
    private String interfaceName;
    private String interfacesHerdadas;





    private myDsl_Type_declaration mydsl_type_declaration;


    public myDsl_Interface_declaration(
        String interfaceHerdada,        String modifiers,        String interfaceName,        String interfacesHerdadas    ) {
        this.interfaceHerdada = interfaceHerdada;
        this.modifiers = modifiers;
        this.interfaceName = interfaceName;
        this.interfacesHerdadas = interfacesHerdadas;
    }


    public String getInterfaceherdada() {
        return interfaceHerdada;
    }

    public void setInterfaceherdada(String interfaceHerdada) {
        this.interfaceHerdada = interfaceHerdada;
    }
    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }
    public String getInterfacename() {
        return interfaceName;
    }

    public void setInterfacename(String interfaceName) {
        this.interfaceName = interfaceName;
    }
    public String getInterfacesherdadas() {
        return interfacesHerdadas;
    }

    public void setInterfacesherdadas(String interfacesHerdadas) {
        this.interfacesHerdadas = interfacesHerdadas;
    }

    public myDsl_Type_declaration getMydsl_type_declaration() {
        return mydsl_type_declaration;
    }

    public void setMydsl_type_declaration(myDsl_Type_declaration mydsl_type_declaration) {
        this.mydsl_type_declaration = mydsl_type_declaration;
    }

}