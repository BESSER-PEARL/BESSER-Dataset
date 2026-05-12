





import java.util.List;
import java.util.ArrayList;

public class publication2014_Progress extends Labelled {

    private int percent;
    private int time;





    private publication2014_Paper publication2014_paper;




    private publication2014_PublicationProcess publication2014_publicationprocess;




    private publication2014_Paper publication2014_paper;


    public publication2014_Progress(
        int percent,        int time    ) {
        super(
        );
        this.percent = percent;
        this.time = time;
    }


    public int getPercent() {
        return percent;
    }

    public void setPercent(int percent) {
        this.percent = percent;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public publication2014_Paper getPublication2014_paper() {
        return publication2014_paper;
    }

    public void setPublication2014_paper(publication2014_Paper publication2014_paper) {
        this.publication2014_paper = publication2014_paper;
    }
    public publication2014_PublicationProcess getPublication2014_publicationprocess() {
        return publication2014_publicationprocess;
    }

    public void setPublication2014_publicationprocess(publication2014_PublicationProcess publication2014_publicationprocess) {
        this.publication2014_publicationprocess = publication2014_publicationprocess;
    }
    public publication2014_Paper getPublication2014_paper() {
        return publication2014_paper;
    }

    public void setPublication2014_paper(publication2014_Paper publication2014_paper) {
        this.publication2014_paper = publication2014_paper;
    }

}