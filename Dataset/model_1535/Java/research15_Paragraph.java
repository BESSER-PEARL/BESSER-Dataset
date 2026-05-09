





import java.util.List;
import java.util.ArrayList;

public class research15_Paragraph extends Counted, Named {

    private String content;





    private research15_Paper research15_paper;


    public research15_Paragraph(
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

    public research15_Paper getResearch15_paper() {
        return research15_paper;
    }

    public void setResearch15_paper(research15_Paper research15_paper) {
        this.research15_paper = research15_paper;
    }

}