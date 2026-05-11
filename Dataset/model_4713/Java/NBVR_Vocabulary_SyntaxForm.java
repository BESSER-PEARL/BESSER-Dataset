





import java.util.List;
import java.util.ArrayList;

public class NBVR_Vocabulary_SyntaxForm  {

    private boolean isAuxForm;
    private String text;





    private VocVerb vocverb;




    private VocProperty vocproperty;


    public NBVR_Vocabulary_SyntaxForm(
        boolean isAuxForm,        String text    ) {
        this.isAuxForm = isAuxForm;
        this.text = text;
    }


    public boolean getIsauxform() {
        return isAuxForm;
    }

    public void setIsauxform(boolean isAuxForm) {
        this.isAuxForm = isAuxForm;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public VocVerb getVocverb() {
        return vocverb;
    }

    public void setVocverb(VocVerb vocverb) {
        this.vocverb = vocverb;
    }
    public VocProperty getVocproperty() {
        return vocproperty;
    }

    public void setVocproperty(VocProperty vocproperty) {
        this.vocproperty = vocproperty;
    }

}