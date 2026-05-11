





import java.util.List;
import java.util.ArrayList;

public class class_diagramm_Method extends RefMethod {

    private String name;
    private String modifier;





    private class_diagramm_RefClass class_diagramm_refclass;


    public class_diagramm_Method(
        String name,        String modifier    ) {
        super(
        );
        this.name = name;
        this.modifier = modifier;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }

    public class_diagramm_RefClass getClass_diagramm_refclass() {
        return class_diagramm_refclass;
    }

    public void setClass_diagramm_refclass(class_diagramm_RefClass class_diagramm_refclass) {
        this.class_diagramm_refclass = class_diagramm_refclass;
    }

}