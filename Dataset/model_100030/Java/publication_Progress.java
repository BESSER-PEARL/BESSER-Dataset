





import java.util.List;
import java.util.ArrayList;

public class publication_Progress extends Labelled {

    private int time;
    private int percent;





    private publication_PublicationProcess publication_publicationprocess;




    private publication_Paper publication_paper;




    private publication_Paper publication_paper;


    public publication_Progress(
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

    public publication_PublicationProcess getPublication_publicationprocess() {
        return publication_publicationprocess;
    }

    public void setPublication_publicationprocess(publication_PublicationProcess publication_publicationprocess) {
        this.publication_publicationprocess = publication_publicationprocess;
    }
    public publication_Paper getPublication_paper() {
        return publication_paper;
    }

    public void setPublication_paper(publication_Paper publication_paper) {
        this.publication_paper = publication_paper;
    }
    public publication_Paper getPublication_paper() {
        return publication_paper;
    }

    public void setPublication_paper(publication_Paper publication_paper) {
        this.publication_paper = publication_paper;
    }

}