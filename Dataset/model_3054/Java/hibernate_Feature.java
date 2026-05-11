





import java.util.List;
import java.util.ArrayList;

public class hibernate_Feature extends NamedElement {

    private boolean many;
    private String annotations;



    public hibernate_Feature(
        boolean many,        String annotations    ) {
        super(
        );
        this.many = many;
        this.annotations = annotations;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getAnnotations() {
        return annotations;
    }

    public void setAnnotations(String annotations) {
        this.annotations = annotations;
    }


}