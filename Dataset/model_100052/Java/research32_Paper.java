





import java.util.List;
import java.util.ArrayList;

public class research32_Paper extends Named {






    private List<research32_Paragraph> research32_paragraphs;




    private research32_Paper research32_paper;




    private List<research32_Researcher> research32_researchers;




    private research32_Keyword research32_keyword;




    private research32_PublicationStructure research32_publicationstructure;




    private research32_Researcher research32_researcher;


    public research32_Paper(
    ) {
        super(
        );
        this.research32_paragraphs = new ArrayList<>();
        this.research32_researchers = new ArrayList<>();
    }

    public research32_Paper(
        ArrayList<research32_Paragraph> research32_paragraphs,        ArrayList<research32_Researcher> research32_researchers    ) {
        this.research32_paragraphs = research32_paragraphs;
        this.research32_researchers = research32_researchers;
    }


    public List<research32_Paragraph> getResearch32_paragraphs() {
        return research32_paragraphs;
    }

    public void addResearch32_paragraph(Research32_paragraph research32_paragraph) {
        this.research32_paragraphs.add(research32_paragraph);
    }
    public research32_Paper getResearch32_paper() {
        return research32_paper;
    }

    public void setResearch32_paper(research32_Paper research32_paper) {
        this.research32_paper = research32_paper;
    }
    public List<research32_Researcher> getResearch32_researchers() {
        return research32_researchers;
    }

    public void addResearch32_researcher(Research32_researcher research32_researcher) {
        this.research32_researchers.add(research32_researcher);
    }
    public research32_Keyword getResearch32_keyword() {
        return research32_keyword;
    }

    public void setResearch32_keyword(research32_Keyword research32_keyword) {
        this.research32_keyword = research32_keyword;
    }
    public research32_PublicationStructure getResearch32_publicationstructure() {
        return research32_publicationstructure;
    }

    public void setResearch32_publicationstructure(research32_PublicationStructure research32_publicationstructure) {
        this.research32_publicationstructure = research32_publicationstructure;
    }
    public research32_Researcher getResearch32_researcher() {
        return research32_researcher;
    }

    public void setResearch32_researcher(research32_Researcher research32_researcher) {
        this.research32_researcher = research32_researcher;
    }

}