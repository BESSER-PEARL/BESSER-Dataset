





import java.util.List;
import java.util.ArrayList;

public class class_diagramm_Attribute extends RefAttribute {

    private String name;
    private String modifier;





    private class_diagramm_RefDataType class_diagramm_refdatatype;




    private class_diagramm_RefClass class_diagramm_refclass;


    public class_diagramm_Attribute(
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

    public class_diagramm_RefDataType getClass_diagramm_refdatatype() {
        return class_diagramm_refdatatype;
    }

    public void setClass_diagramm_refdatatype(class_diagramm_RefDataType class_diagramm_refdatatype) {
        this.class_diagramm_refdatatype = class_diagramm_refdatatype;
    }
    public class_diagramm_RefClass getClass_diagramm_refclass() {
        return class_diagramm_refclass;
    }

    public void setClass_diagramm_refclass(class_diagramm_RefClass class_diagramm_refclass) {
        this.class_diagramm_refclass = class_diagramm_refclass;
    }

}