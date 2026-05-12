





import java.util.List;
import java.util.ArrayList;

public class research20_Paragraph extends Counted, Named {

    private String content;





    private research20_Paper research20_paper;


    public research20_Paragraph(
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

    public research20_Paper getResearch20_paper() {
        return research20_paper;
    }

    public void setResearch20_paper(research20_Paper research20_paper) {
        this.research20_paper = research20_paper;
    }

}