





import java.util.List;
import java.util.ArrayList;

public class LaTeX_DocumentBody  {






    private List<Section> sections;




    private List<Bibliography> bibliographys;


    public LaTeX_DocumentBody(
    ) {
        this.sections = new ArrayList<>();
        this.bibliographys = new ArrayList<>();
    }

    public LaTeX_DocumentBody(
        ArrayList<Section> sections,        ArrayList<Bibliography> bibliographys    ) {
        this.sections = sections;
        this.bibliographys = bibliographys;
    }


    public List<Section> getSections() {
        return sections;
    }

    public void addSection(Section section) {
        this.sections.add(section);
    }
    public List<Bibliography> getBibliographys() {
        return bibliographys;
    }

    public void addBibliography(Bibliography bibliography) {
        this.bibliographys.add(bibliography);
    }

}