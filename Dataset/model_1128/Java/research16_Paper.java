





import java.util.List;
import java.util.ArrayList;

public class research16_Paper extends Named {






    private research16_Paper research16_paper;




    private List<research16_Paragraph> research16_paragraphs;


    public research16_Paper(
    ) {
        super(
        );
        this.research16_paragraphs = new ArrayList<>();
    }

    public research16_Paper(
        ArrayList<research16_Paragraph> research16_paragraphs    ) {
        this.research16_paragraphs = research16_paragraphs;
    }


    public research16_Paper getResearch16_paper() {
        return research16_paper;
    }

    public void setResearch16_paper(research16_Paper research16_paper) {
        this.research16_paper = research16_paper;
    }
    public List<research16_Paragraph> getResearch16_paragraphs() {
        return research16_paragraphs;
    }

    public void addResearch16_paragraph(Research16_paragraph research16_paragraph) {
        this.research16_paragraphs.add(research16_paragraph);
    }

}