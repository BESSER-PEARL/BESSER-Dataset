





import java.util.List;
import java.util.ArrayList;

public class p2_FeatureMetadata extends LocatedElement {

    private String text;
    private String name;



    public p2_FeatureMetadata(
        String text,        String name    ) {
        super(
        );
        this.text = text;
        this.name = name;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}