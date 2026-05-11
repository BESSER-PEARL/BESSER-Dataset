





import java.util.List;
import java.util.ArrayList;

public class class_diagramm_Class extends RefClass {

    private String name;
    private String modifier;





    private List<class_diagramm_RefMethod> class_diagramm_refmethods;




    private List<class_diagramm_RefAttribute> class_diagramm_refattributes;




    private class_diagramm_RefClass class_diagramm_refclass;


    public class_diagramm_Class(
        String name,        String modifier    ) {
        super(
        );
        this.name = name;
        this.modifier = modifier;
        this.class_diagramm_refmethods = new ArrayList<>();
        this.class_diagramm_refattributes = new ArrayList<>();
    }

    public class_diagramm_Class(
        String name,        String modifier        ArrayList<class_diagramm_RefMethod> class_diagramm_refmethods,        ArrayList<class_diagramm_RefAttribute> class_diagramm_refattributes    ) {
        this.name = name;
        this.modifier = modifier;
        this.class_diagramm_refmethods = class_diagramm_refmethods;
        this.class_diagramm_refattributes = class_diagramm_refattributes;
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

    public List<class_diagramm_RefMethod> getClass_diagramm_refmethods() {
        return class_diagramm_refmethods;
    }

    public void addClass_diagramm_refmethod(Class_diagramm_refmethod class_diagramm_refmethod) {
        this.class_diagramm_refmethods.add(class_diagramm_refmethod);
    }
    public List<class_diagramm_RefAttribute> getClass_diagramm_refattributes() {
        return class_diagramm_refattributes;
    }

    public void addClass_diagramm_refattribute(Class_diagramm_refattribute class_diagramm_refattribute) {
        this.class_diagramm_refattributes.add(class_diagramm_refattribute);
    }
    public class_diagramm_RefClass getClass_diagramm_refclass() {
        return class_diagramm_refclass;
    }

    public void setClass_diagramm_refclass(class_diagramm_RefClass class_diagramm_refclass) {
        this.class_diagramm_refclass = class_diagramm_refclass;
    }

}