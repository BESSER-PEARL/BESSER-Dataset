





import java.util.List;
import java.util.ArrayList;

public class research18_Paper extends Named {






    private research18_Paper research18_paper;




    private research18_PublicationStructure research18_publicationstructure;




    private research18_Keyword research18_keyword;




    private List<research18_Paragraph> research18_paragraphs;


    public research18_Paper(
    ) {
        super(
        );
        this.research18_paragraphs = new ArrayList<>();
    }

    public research18_Paper(
        ArrayList<research18_Paragraph> research18_paragraphs    ) {
        this.research18_paragraphs = research18_paragraphs;
    }


    public research18_Paper getResearch18_paper() {
        return research18_paper;
    }

    public void setResearch18_paper(research18_Paper research18_paper) {
        this.research18_paper = research18_paper;
    }
    public research18_PublicationStructure getResearch18_publicationstructure() {
        return research18_publicationstructure;
    }

    public void setResearch18_publicationstructure(research18_PublicationStructure research18_publicationstructure) {
        this.research18_publicationstructure = research18_publicationstructure;
    }
    public research18_Keyword getResearch18_keyword() {
        return research18_keyword;
    }

    public void setResearch18_keyword(research18_Keyword research18_keyword) {
        this.research18_keyword = research18_keyword;
    }
    public List<research18_Paragraph> getResearch18_paragraphs() {
        return research18_paragraphs;
    }

    public void addResearch18_paragraph(Research18_paragraph research18_paragraph) {
        this.research18_paragraphs.add(research18_paragraph);
    }

}