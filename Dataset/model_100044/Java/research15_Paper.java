





import java.util.List;
import java.util.ArrayList;

public class research15_Paper extends Named {






    private research15_PublicationStructure research15_publicationstructure;




    private research15_Keyword research15_keyword;




    private research15_Paper research15_paper;




    private List<research15_Paragraph> research15_paragraphs;


    public research15_Paper(
    ) {
        super(
        );
        this.research15_paragraphs = new ArrayList<>();
    }

    public research15_Paper(
        ArrayList<research15_Paragraph> research15_paragraphs    ) {
        this.research15_paragraphs = research15_paragraphs;
    }


    public research15_PublicationStructure getResearch15_publicationstructure() {
        return research15_publicationstructure;
    }

    public void setResearch15_publicationstructure(research15_PublicationStructure research15_publicationstructure) {
        this.research15_publicationstructure = research15_publicationstructure;
    }
    public research15_Keyword getResearch15_keyword() {
        return research15_keyword;
    }

    public void setResearch15_keyword(research15_Keyword research15_keyword) {
        this.research15_keyword = research15_keyword;
    }
    public research15_Paper getResearch15_paper() {
        return research15_paper;
    }

    public void setResearch15_paper(research15_Paper research15_paper) {
        this.research15_paper = research15_paper;
    }
    public List<research15_Paragraph> getResearch15_paragraphs() {
        return research15_paragraphs;
    }

    public void addResearch15_paragraph(Research15_paragraph research15_paragraph) {
        this.research15_paragraphs.add(research15_paragraph);
    }

}