





import java.util.List;
import java.util.ArrayList;

public class research101_Paper extends Named {






    private List<research101_Paragraph> research101_paragraphs;




    private research101_Paper research101_paper;




    private research101_Keyword research101_keyword;


    public research101_Paper(
    ) {
        super(
        );
        this.research101_paragraphs = new ArrayList<>();
    }

    public research101_Paper(
        ArrayList<research101_Paragraph> research101_paragraphs    ) {
        this.research101_paragraphs = research101_paragraphs;
    }


    public List<research101_Paragraph> getResearch101_paragraphs() {
        return research101_paragraphs;
    }

    public void addResearch101_paragraph(Research101_paragraph research101_paragraph) {
        this.research101_paragraphs.add(research101_paragraph);
    }
    public research101_Paper getResearch101_paper() {
        return research101_paper;
    }

    public void setResearch101_paper(research101_Paper research101_paper) {
        this.research101_paper = research101_paper;
    }
    public research101_Keyword getResearch101_keyword() {
        return research101_keyword;
    }

    public void setResearch101_keyword(research101_Keyword research101_keyword) {
        this.research101_keyword = research101_keyword;
    }

}