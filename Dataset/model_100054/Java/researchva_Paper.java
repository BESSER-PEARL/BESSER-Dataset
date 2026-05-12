





import java.util.List;
import java.util.ArrayList;

public class researchva_Paper extends Named {






    private researchva_Researcher researchva_researcher;




    private researchva_Paper researchva_paper;




    private List<researchva_Paragraph> researchva_paragraphs;




    private List<researchva_Researcher> researchva_researchers;


    public researchva_Paper(
    ) {
        super(
        );
        this.researchva_paragraphs = new ArrayList<>();
        this.researchva_researchers = new ArrayList<>();
    }

    public researchva_Paper(
        ArrayList<researchva_Paragraph> researchva_paragraphs,        ArrayList<researchva_Researcher> researchva_researchers    ) {
        this.researchva_paragraphs = researchva_paragraphs;
        this.researchva_researchers = researchva_researchers;
    }


    public researchva_Researcher getResearchva_researcher() {
        return researchva_researcher;
    }

    public void setResearchva_researcher(researchva_Researcher researchva_researcher) {
        this.researchva_researcher = researchva_researcher;
    }
    public researchva_Paper getResearchva_paper() {
        return researchva_paper;
    }

    public void setResearchva_paper(researchva_Paper researchva_paper) {
        this.researchva_paper = researchva_paper;
    }
    public List<researchva_Paragraph> getResearchva_paragraphs() {
        return researchva_paragraphs;
    }

    public void addResearchva_paragraph(Researchva_paragraph researchva_paragraph) {
        this.researchva_paragraphs.add(researchva_paragraph);
    }
    public List<researchva_Researcher> getResearchva_researchers() {
        return researchva_researchers;
    }

    public void addResearchva_researcher(Researchva_researcher researchva_researcher) {
        this.researchva_researchers.add(researchva_researcher);
    }

}