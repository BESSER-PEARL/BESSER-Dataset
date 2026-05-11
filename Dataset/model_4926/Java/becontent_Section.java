





import java.util.List;
import java.util.ArrayList;

public class becontent_Section extends NotStructuredElement {

    private String name;
    private String text;



    public becontent_Section(
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