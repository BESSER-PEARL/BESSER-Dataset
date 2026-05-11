





import java.util.List;
import java.util.ArrayList;

public class lobj_HypertextContent extends AbstractContent {

    private String content;





    private lobj_HypertextBlock lobj_hypertextblock;


    public lobj_HypertextContent(
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

    public lobj_HypertextBlock getLobj_hypertextblock() {
        return lobj_hypertextblock;
    }

    public void setLobj_hypertextblock(lobj_HypertextBlock lobj_hypertextblock) {
        this.lobj_hypertextblock = lobj_hypertextblock;
    }

}