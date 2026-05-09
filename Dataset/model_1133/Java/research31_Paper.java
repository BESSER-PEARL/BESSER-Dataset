





import java.util.List;
import java.util.ArrayList;

public class research31_Paper extends Named {






    private research31_Keyword research31_keyword;




    private research31_Paper research31_paper;




    private List<research31_Paragraph> research31_paragraphs;


    public research31_Paper(
    ) {
        super(
        );
        this.research31_paragraphs = new ArrayList<>();
    }

    public research31_Paper(
        ArrayList<research31_Paragraph> research31_paragraphs    ) {
        this.research31_paragraphs = research31_paragraphs;
    }


    public research31_Keyword getResearch31_keyword() {
        return research31_keyword;
    }

    public void setResearch31_keyword(research31_Keyword research31_keyword) {
        this.research31_keyword = research31_keyword;
    }
    public research31_Paper getResearch31_paper() {
        return research31_paper;
    }

    public void setResearch31_paper(research31_Paper research31_paper) {
        this.research31_paper = research31_paper;
    }
    public List<research31_Paragraph> getResearch31_paragraphs() {
        return research31_paragraphs;
    }

    public void addResearch31_paragraph(Research31_paragraph research31_paragraph) {
        this.research31_paragraphs.add(research31_paragraph);
    }

}