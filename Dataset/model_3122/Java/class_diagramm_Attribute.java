





import java.util.List;
import java.util.ArrayList;

public class class_diagramm_Attribute extends RefAttribute {

    private String name;
    private String modifier;



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


}