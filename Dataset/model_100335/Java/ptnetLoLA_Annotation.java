





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_Annotation  {

    private String text;





    private ptnetLoLA_PtNet ptnetlola_ptnet;




    private ptnetLoLA_Node ptnetlola_node;


    public ptnetLoLA_Annotation(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public ptnetLoLA_PtNet getPtnetlola_ptnet() {
        return ptnetlola_ptnet;
    }

    public void setPtnetlola_ptnet(ptnetLoLA_PtNet ptnetlola_ptnet) {
        this.ptnetlola_ptnet = ptnetlola_ptnet;
    }
    public ptnetLoLA_Node getPtnetlola_node() {
        return ptnetlola_node;
    }

    public void setPtnetlola_node(ptnetLoLA_Node ptnetlola_node) {
        this.ptnetlola_node = ptnetlola_node;
    }

}