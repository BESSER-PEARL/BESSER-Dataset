





import java.util.List;
import java.util.ArrayList;

public class cpntools_TransPriority extends DiagramElement {

    private String text;





    private cpntools_Trans cpntools_trans;


    public cpntools_TransPriority(
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

    public cpntools_Trans getCpntools_trans() {
        return cpntools_trans;
    }

    public void setCpntools_trans(cpntools_Trans cpntools_trans) {
        this.cpntools_trans = cpntools_trans;
    }

}