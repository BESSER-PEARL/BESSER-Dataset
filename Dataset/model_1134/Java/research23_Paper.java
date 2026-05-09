





import java.util.List;
import java.util.ArrayList;

public class research23_Paper extends Named {






    private List<research23_Paragraph> research23_paragraphs;




    private research23_PublicationStructure research23_publicationstructure;




    private research23_Paper research23_paper;




    private research23_Keyword research23_keyword;


    public research23_Paper(
    ) {
        super(
        );
        this.research23_paragraphs = new ArrayList<>();
    }

    public research23_Paper(
        ArrayList<research23_Paragraph> research23_paragraphs    ) {
        this.research23_paragraphs = research23_paragraphs;
    }


    public List<research23_Paragraph> getResearch23_paragraphs() {
        return research23_paragraphs;
    }

    public void addResearch23_paragraph(Research23_paragraph research23_paragraph) {
        this.research23_paragraphs.add(research23_paragraph);
    }
    public research23_PublicationStructure getResearch23_publicationstructure() {
        return research23_publicationstructure;
    }

    public void setResearch23_publicationstructure(research23_PublicationStructure research23_publicationstructure) {
        this.research23_publicationstructure = research23_publicationstructure;
    }
    public research23_Paper getResearch23_paper() {
        return research23_paper;
    }

    public void setResearch23_paper(research23_Paper research23_paper) {
        this.research23_paper = research23_paper;
    }
    public research23_Keyword getResearch23_keyword() {
        return research23_keyword;
    }

    public void setResearch23_keyword(research23_Keyword research23_keyword) {
        this.research23_keyword = research23_keyword;
    }

}