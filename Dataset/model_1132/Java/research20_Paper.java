





import java.util.List;
import java.util.ArrayList;

public class research20_Paper extends Named {






    private research20_PublicationStructure research20_publicationstructure;




    private research20_Paper research20_paper;




    private research20_Keyword research20_keyword;




    private List<research20_Paragraph> research20_paragraphs;


    public research20_Paper(
    ) {
        super(
        );
        this.research20_paragraphs = new ArrayList<>();
    }

    public research20_Paper(
        ArrayList<research20_Paragraph> research20_paragraphs    ) {
        this.research20_paragraphs = research20_paragraphs;
    }


    public research20_PublicationStructure getResearch20_publicationstructure() {
        return research20_publicationstructure;
    }

    public void setResearch20_publicationstructure(research20_PublicationStructure research20_publicationstructure) {
        this.research20_publicationstructure = research20_publicationstructure;
    }
    public research20_Paper getResearch20_paper() {
        return research20_paper;
    }

    public void setResearch20_paper(research20_Paper research20_paper) {
        this.research20_paper = research20_paper;
    }
    public research20_Keyword getResearch20_keyword() {
        return research20_keyword;
    }

    public void setResearch20_keyword(research20_Keyword research20_keyword) {
        this.research20_keyword = research20_keyword;
    }
    public List<research20_Paragraph> getResearch20_paragraphs() {
        return research20_paragraphs;
    }

    public void addResearch20_paragraph(Research20_paragraph research20_paragraph) {
        this.research20_paragraphs.add(research20_paragraph);
    }

}