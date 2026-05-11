





import java.util.List;
import java.util.ArrayList;

public class class_diagramm_Class extends RefClass {

    private String modifier;
    private String name;



    public class_diagramm_Class(
        String modifier,        String name    ) {
        super(
        );
        this.modifier = modifier;
        this.name = name;
    }


    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}