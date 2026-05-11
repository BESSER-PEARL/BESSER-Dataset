





import java.util.List;
import java.util.ArrayList;

public class go_Atrib extends varFor {

    private String type;
    private String modifier;
    private String name;



    public go_Atrib(
        String type,        String modifier,        String name    ) {
        super(
        );
        this.type = type;
        this.modifier = modifier;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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