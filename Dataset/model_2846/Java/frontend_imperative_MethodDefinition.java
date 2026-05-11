





import java.util.List;
import java.util.ArrayList;

public class frontend_imperative_MethodDefinition extends LocatedElement {

    private String name;





    private ClassUse classuse;


    public frontend_imperative_MethodDefinition(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassUse getClassuse() {
        return classuse;
    }

    public void setClassuse(ClassUse classuse) {
        this.classuse = classuse;
    }

}