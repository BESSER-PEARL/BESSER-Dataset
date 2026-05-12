





import java.util.List;
import java.util.ArrayList;

public class publication2014b_Progress extends Labelled {

    private int time;
    private int percent;





    private publication2014b_Paper publication2014b_paper;




    private publication2014b_PublicationProcess publication2014b_publicationprocess;




    private publication2014b_Paper publication2014b_paper;


    public publication2014b_Progress(
        int time,        int percent    ) {
        super(
        );
        this.time = time;
        this.percent = percent;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public int getPercent() {
        return percent;
    }

    public void setPercent(int percent) {
        this.percent = percent;
    }

    public publication2014b_Paper getPublication2014b_paper() {
        return publication2014b_paper;
    }

    public void setPublication2014b_paper(publication2014b_Paper publication2014b_paper) {
        this.publication2014b_paper = publication2014b_paper;
    }
    public publication2014b_PublicationProcess getPublication2014b_publicationprocess() {
        return publication2014b_publicationprocess;
    }

    public void setPublication2014b_publicationprocess(publication2014b_PublicationProcess publication2014b_publicationprocess) {
        this.publication2014b_publicationprocess = publication2014b_publicationprocess;
    }
    public publication2014b_Paper getPublication2014b_paper() {
        return publication2014b_paper;
    }

    public void setPublication2014b_paper(publication2014b_Paper publication2014b_paper) {
        this.publication2014b_paper = publication2014b_paper;
    }

}