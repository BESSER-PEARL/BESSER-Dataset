





import java.util.List;
import java.util.ArrayList;

public class mention_graph_Node  {

    private String value;





    private mention_graph_MentionGraph mention_graph_mentiongraph;


    public mention_graph_Node(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public mention_graph_MentionGraph getMention_graph_mentiongraph() {
        return mention_graph_mentiongraph;
    }

    public void setMention_graph_mentiongraph(mention_graph_MentionGraph mention_graph_mentiongraph) {
        this.mention_graph_mentiongraph = mention_graph_mentiongraph;
    }

}