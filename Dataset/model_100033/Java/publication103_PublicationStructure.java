





import java.util.List;
import java.util.ArrayList;

public class publication103_PublicationStructure extends Named {






    private List<publication103_Researcher> publication103_researchers;




    private List<publication103_Paper> publication103_papers;


    public publication103_PublicationStructure(
    ) {
        super(
        );
        this.publication103_researchers = new ArrayList<>();
        this.publication103_papers = new ArrayList<>();
    }

    public publication103_PublicationStructure(
        ArrayList<publication103_Researcher> publication103_researchers,        ArrayList<publication103_Paper> publication103_papers    ) {
        this.publication103_researchers = publication103_researchers;
        this.publication103_papers = publication103_papers;
    }


    public List<publication103_Researcher> getPublication103_researchers() {
        return publication103_researchers;
    }

    public void addPublication103_researcher(Publication103_researcher publication103_researcher) {
        this.publication103_researchers.add(publication103_researcher);
    }
    public List<publication103_Paper> getPublication103_papers() {
        return publication103_papers;
    }

    public void addPublication103_paper(Publication103_paper publication103_paper) {
        this.publication103_papers.add(publication103_paper);
    }

}