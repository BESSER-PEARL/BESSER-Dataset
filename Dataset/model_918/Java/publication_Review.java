





import java.util.List;
import java.util.ArrayList;

public class publication_Review extends Labelled {






    private publication_Researcher publication_researcher;




    private publication_ReviewNote publication_reviewnote;


    public publication_Review(
    ) {
        super(
        );
    }



    public publication_Researcher getPublication_researcher() {
        return publication_researcher;
    }

    public void setPublication_researcher(publication_Researcher publication_researcher) {
        this.publication_researcher = publication_researcher;
    }
    public publication_ReviewNote getPublication_reviewnote() {
        return publication_reviewnote;
    }

    public void setPublication_reviewnote(publication_ReviewNote publication_reviewnote) {
        this.publication_reviewnote = publication_reviewnote;
    }

}