





import java.util.List;
import java.util.ArrayList;

public class research_Progress extends Labelled {

    private int percent;





    private research_Paper research_paper;




    private research_PublicationProcess research_publicationprocess;




    private research_Paper research_paper;


    public research_Progress(
        int percent    ) {
        super(
        );
        this.percent = percent;
    }


    public int getPercent() {
        return percent;
    }

    public void setPercent(int percent) {
        this.percent = percent;
    }

    public research_Paper getResearch_paper() {
        return research_paper;
    }

    public void setResearch_paper(research_Paper research_paper) {
        this.research_paper = research_paper;
    }
    public research_PublicationProcess getResearch_publicationprocess() {
        return research_publicationprocess;
    }

    public void setResearch_publicationprocess(research_PublicationProcess research_publicationprocess) {
        this.research_publicationprocess = research_publicationprocess;
    }
    public research_Paper getResearch_paper() {
        return research_paper;
    }

    public void setResearch_paper(research_Paper research_paper) {
        this.research_paper = research_paper;
    }

}