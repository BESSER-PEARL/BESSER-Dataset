





import java.util.List;
import java.util.ArrayList;

public class research13_Paper extends Named {






    private research13_Keyword research13_keyword;




    private research13_Paper research13_paper;




    private List<research13_Paragraph> research13_paragraphs;




    private research13_PublicationStructure research13_publicationstructure;


    public research13_Paper(
    ) {
        super(
        );
        this.research13_paragraphs = new ArrayList<>();
    }

    public research13_Paper(
        ArrayList<research13_Paragraph> research13_paragraphs    ) {
        this.research13_paragraphs = research13_paragraphs;
    }


    public research13_Keyword getResearch13_keyword() {
        return research13_keyword;
    }

    public void setResearch13_keyword(research13_Keyword research13_keyword) {
        this.research13_keyword = research13_keyword;
    }
    public research13_Paper getResearch13_paper() {
        return research13_paper;
    }

    public void setResearch13_paper(research13_Paper research13_paper) {
        this.research13_paper = research13_paper;
    }
    public List<research13_Paragraph> getResearch13_paragraphs() {
        return research13_paragraphs;
    }

    public void addResearch13_paragraph(Research13_paragraph research13_paragraph) {
        this.research13_paragraphs.add(research13_paragraph);
    }
    public research13_PublicationStructure getResearch13_publicationstructure() {
        return research13_publicationstructure;
    }

    public void setResearch13_publicationstructure(research13_PublicationStructure research13_publicationstructure) {
        this.research13_publicationstructure = research13_publicationstructure;
    }

}