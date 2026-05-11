





import java.util.List;
import java.util.ArrayList;

public class sample_Comment  {

    private String content;





    private sample_Node sample_node;


    public sample_Comment(
        String content    ) {
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public sample_Node getSample_node() {
        return sample_node;
    }

    public void setSample_node(sample_Node sample_node) {
        this.sample_node = sample_node;
    }

}