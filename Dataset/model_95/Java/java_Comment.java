





import java.util.List;
import java.util.ArrayList;

public class java_Comment extends ASTNode {

    private String content;



    public java_Comment(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}