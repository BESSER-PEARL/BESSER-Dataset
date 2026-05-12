





import java.util.List;
import java.util.ArrayList;

public class LaTeX_Citation  {






    private Description description;




    private Bibliography bibliography;




    private Author author;




    private Label label;


    public LaTeX_Citation(
    ) {
    }



    public Description getDescription() {
        return description;
    }

    public void setDescription(Description description) {
        this.description = description;
    }
    public Bibliography getBibliography() {
        return bibliography;
    }

    public void setBibliography(Bibliography bibliography) {
        this.bibliography = bibliography;
    }
    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }
    public Label getLabel() {
        return label;
    }

    public void setLabel(Label label) {
        this.label = label;
    }

}