





import java.util.List;
import java.util.ArrayList;

public class cpntools_Annot extends DiagramElement {

    private String text;





    private cpntools_Arc cpntools_arc;


    public cpntools_Annot(
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

    public cpntools_Arc getCpntools_arc() {
        return cpntools_arc;
    }

    public void setCpntools_arc(cpntools_Arc cpntools_arc) {
        this.cpntools_arc = cpntools_arc;
    }

}