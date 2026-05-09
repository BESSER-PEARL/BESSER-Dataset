





import java.util.List;
import java.util.ArrayList;

public class javaDsl_InterfaceMemberDeclaration  {

    private String modifiers;





    private javaDsl_InterfaceBody javadsl_interfacebody;


    public javaDsl_InterfaceMemberDeclaration(
        String modifiers    ) {
        this.modifiers = modifiers;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }

    public javaDsl_InterfaceBody getJavadsl_interfacebody() {
        return javadsl_interfacebody;
    }

    public void setJavadsl_interfacebody(javaDsl_InterfaceBody javadsl_interfacebody) {
        this.javadsl_interfacebody = javadsl_interfacebody;
    }

}