





import java.util.List;
import java.util.ArrayList;

public class mention_graph_HashTag extends Node {

    private int count;





    private mention_graph_User mention_graph_user;


    public mention_graph_HashTag(
        int count    ) {
        super(
        );
        this.count = count;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public mention_graph_User getMention_graph_user() {
        return mention_graph_user;
    }

    public void setMention_graph_user(mention_graph_User mention_graph_user) {
        this.mention_graph_user = mention_graph_user;
    }

}