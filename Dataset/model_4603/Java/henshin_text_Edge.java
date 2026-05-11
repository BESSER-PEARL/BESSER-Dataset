





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Edge  {

    private String actiontype;





    private henshin_text_EReference henshin_text_ereference;




    private henshin_text_Edges henshin_text_edges;


    public henshin_text_Edge(
        String actiontype    ) {
        this.actiontype = actiontype;
    }


    public String getActiontype() {
        return actiontype;
    }

    public void setActiontype(String actiontype) {
        this.actiontype = actiontype;
    }

    public henshin_text_EReference getHenshin_text_ereference() {
        return henshin_text_ereference;
    }

    public void setHenshin_text_ereference(henshin_text_EReference henshin_text_ereference) {
        this.henshin_text_ereference = henshin_text_ereference;
    }
    public henshin_text_Edges getHenshin_text_edges() {
        return henshin_text_edges;
    }

    public void setHenshin_text_edges(henshin_text_Edges henshin_text_edges) {
        this.henshin_text_edges = henshin_text_edges;
    }

}