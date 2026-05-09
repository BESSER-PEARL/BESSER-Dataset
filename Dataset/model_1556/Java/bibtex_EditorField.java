





import java.util.List;
import java.util.ArrayList;

public class bibtex_EditorField extends Field {






    private bibtex_InProceedingsEntry bibtex_inproceedingsentry;




    private List<bibtex_Editor> bibtex_editors;


    public bibtex_EditorField(
    ) {
        super(
        );
        this.bibtex_editors = new ArrayList<>();
    }

    public bibtex_EditorField(
        ArrayList<bibtex_Editor> bibtex_editors    ) {
        this.bibtex_editors = bibtex_editors;
    }


    public bibtex_InProceedingsEntry getBibtex_inproceedingsentry() {
        return bibtex_inproceedingsentry;
    }

    public void setBibtex_inproceedingsentry(bibtex_InProceedingsEntry bibtex_inproceedingsentry) {
        this.bibtex_inproceedingsentry = bibtex_inproceedingsentry;
    }
    public List<bibtex_Editor> getBibtex_editors() {
        return bibtex_editors;
    }

    public void addBibtex_editor(Bibtex_editor bibtex_editor) {
        this.bibtex_editors.add(bibtex_editor);
    }

}