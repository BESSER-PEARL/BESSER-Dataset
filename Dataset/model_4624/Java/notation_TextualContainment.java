





import java.util.List;
import java.util.ArrayList;

public class notation_TextualContainment  {

    private String layout;





    private notation_Label notation_label;




    private List<notation_TextualElement> notation_textualelements;


    public notation_TextualContainment(
        String layout    ) {
        this.layout = layout;
        this.notation_textualelements = new ArrayList<>();
    }

    public notation_TextualContainment(
        String layout        ArrayList<notation_TextualElement> notation_textualelements    ) {
        this.layout = layout;
        this.notation_textualelements = notation_textualelements;
    }

    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }

    public notation_Label getNotation_label() {
        return notation_label;
    }

    public void setNotation_label(notation_Label notation_label) {
        this.notation_label = notation_label;
    }
    public List<notation_TextualElement> getNotation_textualelements() {
        return notation_textualelements;
    }

    public void addNotation_textualelement(Notation_textualelement notation_textualelement) {
        this.notation_textualelements.add(notation_textualelement);
    }

}