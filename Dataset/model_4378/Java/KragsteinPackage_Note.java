





import java.util.List;
import java.util.ArrayList;

public class KragsteinPackage_Note extends Unit {

    private String name;
    private String text;



    public KragsteinPackage_Note(
        String name,        String text    ) {
        super(
        );
        this.name = name;
        this.text = text;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}