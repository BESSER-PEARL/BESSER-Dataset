





import java.util.List;
import java.util.ArrayList;

public class research32_Paper extends Named {






    private research32_Paper research32_paper;




    private research32_Progress research32_progress;




    private research32_Collaboration research32_collaboration;




    private List<research32_Paragraph> research32_paragraphs;




    private List<research32_PaperKeyword> research32_paperkeywords;




    private List<research32_Progress> research32_progresss;


    public research32_Paper(
    ) {
        super(
        );
        this.research32_paragraphs = new ArrayList<>();
        this.research32_paperkeywords = new ArrayList<>();
        this.research32_progresss = new ArrayList<>();
    }

    public research32_Paper(
        ArrayList<research32_Paragraph> research32_paragraphs,        ArrayList<research32_PaperKeyword> research32_paperkeywords,        ArrayList<research32_Progress> research32_progresss    ) {
        this.research32_paragraphs = research32_paragraphs;
        this.research32_paperkeywords = research32_paperkeywords;
        this.research32_progresss = research32_progresss;
    }


    public research32_Paper getResearch32_paper() {
        return research32_paper;
    }

    public void setResearch32_paper(research32_Paper research32_paper) {
        this.research32_paper = research32_paper;
    }
    public research32_Progress getResearch32_progress() {
        return research32_progress;
    }

    public void setResearch32_progress(research32_Progress research32_progress) {
        this.research32_progress = research32_progress;
    }
    public research32_Collaboration getResearch32_collaboration() {
        return research32_collaboration;
    }

    public void setResearch32_collaboration(research32_Collaboration research32_collaboration) {
        this.research32_collaboration = research32_collaboration;
    }
    public List<research32_Paragraph> getResearch32_paragraphs() {
        return research32_paragraphs;
    }

    public void addResearch32_paragraph(Research32_paragraph research32_paragraph) {
        this.research32_paragraphs.add(research32_paragraph);
    }
    public List<research32_PaperKeyword> getResearch32_paperkeywords() {
        return research32_paperkeywords;
    }

    public void addResearch32_paperkeyword(Research32_paperkeyword research32_paperkeyword) {
        this.research32_paperkeywords.add(research32_paperkeyword);
    }
    public List<research32_Progress> getResearch32_progresss() {
        return research32_progresss;
    }

    public void addResearch32_progress(Research32_progress research32_progress) {
        this.research32_progresss.add(research32_progress);
    }

}