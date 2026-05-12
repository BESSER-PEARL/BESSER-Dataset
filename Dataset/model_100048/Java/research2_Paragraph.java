





import java.util.List;
import java.util.ArrayList;

public class research2_Paragraph extends Counted, Named {

    private String content;





    private research2_Paper research2_paper;


    public research2_Paragraph(
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

    public research2_Paper getResearch2_paper() {
        return research2_paper;
    }

    public void setResearch2_paper(research2_Paper research2_paper) {
        this.research2_paper = research2_paper;
    }

}