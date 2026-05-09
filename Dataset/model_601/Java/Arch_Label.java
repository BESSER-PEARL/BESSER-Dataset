





import java.util.List;
import java.util.ArrayList;

public class Arch_Label extends GraphicControl {

    private String text;



    public Arch_Label(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}