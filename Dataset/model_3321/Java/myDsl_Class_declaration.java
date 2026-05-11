





import java.util.List;
import java.util.ArrayList;

public class myDsl_Class_declaration  {

    private String interfaceImplementada;
    private String className;
    private String classHerdada;
    private String interfacesImplementadas;
    private String modifiers;





    private myDsl_Type_declaration mydsl_type_declaration;


    public myDsl_Class_declaration(
        String interfaceImplementada,        String className,        String classHerdada,        String interfacesImplementadas,        String modifiers    ) {
        this.interfaceImplementada = interfaceImplementada;
        this.className = className;
        this.classHerdada = classHerdada;
        this.interfacesImplementadas = interfacesImplementadas;
        this.modifiers = modifiers;
    }


    public String getInterfaceimplementada() {
        return interfaceImplementada;
    }

    public void setInterfaceimplementada(String interfaceImplementada) {
        this.interfaceImplementada = interfaceImplementada;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getClassherdada() {
        return classHerdada;
    }

    public void setClassherdada(String classHerdada) {
        this.classHerdada = classHerdada;
    }
    public String getInterfacesimplementadas() {
        return interfacesImplementadas;
    }

    public void setInterfacesimplementadas(String interfacesImplementadas) {
        this.interfacesImplementadas = interfacesImplementadas;
    }
    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }

    public myDsl_Type_declaration getMydsl_type_declaration() {
        return mydsl_type_declaration;
    }

    public void setMydsl_type_declaration(myDsl_Type_declaration mydsl_type_declaration) {
        this.mydsl_type_declaration = mydsl_type_declaration;
    }

}