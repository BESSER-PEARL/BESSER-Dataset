





import java.util.List;
import java.util.ArrayList;

public class research31_Paper extends Named {






    private List<research31_Researcher> research31_researchers;




    private research31_PublicationStructure research31_publicationstructure;




    private List<research31_Progress> research31_progresss;




    private research31_Researcher research31_researcher;




    private research31_Progress research31_progress;




    private research31_Paper research31_paper;




    private research31_Collaboration research31_collaboration;




    private research31_Keyword research31_keyword;




    private List<research31_PaperKeyword> research31_paperkeywords;




    private research31_State research31_state;




    private List<research31_Paragraph> research31_paragraphs;


    public research31_Paper(
    ) {
        super(
        );
        this.research31_researchers = new ArrayList<>();
        this.research31_progresss = new ArrayList<>();
        this.research31_paperkeywords = new ArrayList<>();
        this.research31_paragraphs = new ArrayList<>();
    }

    public research31_Paper(
        ArrayList<research31_Researcher> research31_researchers,        ArrayList<research31_Progress> research31_progresss,        ArrayList<research31_PaperKeyword> research31_paperkeywords,        ArrayList<research31_Paragraph> research31_paragraphs    ) {
        this.research31_researchers = research31_researchers;
        this.research31_progresss = research31_progresss;
        this.research31_paperkeywords = research31_paperkeywords;
        this.research31_paragraphs = research31_paragraphs;
    }


    public List<research31_Researcher> getResearch31_researchers() {
        return research31_researchers;
    }

    public void addResearch31_researcher(Research31_researcher research31_researcher) {
        this.research31_researchers.add(research31_researcher);
    }
    public research31_PublicationStructure getResearch31_publicationstructure() {
        return research31_publicationstructure;
    }

    public void setResearch31_publicationstructure(research31_PublicationStructure research31_publicationstructure) {
        this.research31_publicationstructure = research31_publicationstructure;
    }
    public List<research31_Progress> getResearch31_progresss() {
        return research31_progresss;
    }

    public void addResearch31_progress(Research31_progress research31_progress) {
        this.research31_progresss.add(research31_progress);
    }
    public research31_Researcher getResearch31_researcher() {
        return research31_researcher;
    }

    public void setResearch31_researcher(research31_Researcher research31_researcher) {
        this.research31_researcher = research31_researcher;
    }
    public research31_Progress getResearch31_progress() {
        return research31_progress;
    }

    public void setResearch31_progress(research31_Progress research31_progress) {
        this.research31_progress = research31_progress;
    }
    public research31_Paper getResearch31_paper() {
        return research31_paper;
    }

    public void setResearch31_paper(research31_Paper research31_paper) {
        this.research31_paper = research31_paper;
    }
    public research31_Collaboration getResearch31_collaboration() {
        return research31_collaboration;
    }

    public void setResearch31_collaboration(research31_Collaboration research31_collaboration) {
        this.research31_collaboration = research31_collaboration;
    }
    public research31_Keyword getResearch31_keyword() {
        return research31_keyword;
    }

    public void setResearch31_keyword(research31_Keyword research31_keyword) {
        this.research31_keyword = research31_keyword;
    }
    public List<research31_PaperKeyword> getResearch31_paperkeywords() {
        return research31_paperkeywords;
    }

    public void addResearch31_paperkeyword(Research31_paperkeyword research31_paperkeyword) {
        this.research31_paperkeywords.add(research31_paperkeyword);
    }
    public research31_State getResearch31_state() {
        return research31_state;
    }

    public void setResearch31_state(research31_State research31_state) {
        this.research31_state = research31_state;
    }
    public List<research31_Paragraph> getResearch31_paragraphs() {
        return research31_paragraphs;
    }

    public void addResearch31_paragraph(Research31_paragraph research31_paragraph) {
        this.research31_paragraphs.add(research31_paragraph);
    }

}