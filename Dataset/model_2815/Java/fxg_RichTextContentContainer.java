





import java.util.List;
import java.util.ArrayList;

public class fxg_RichTextContentContainer extends RichTextContent {






    private List<fxg_RichTextContent> fxg_richtextcontents;


    public fxg_RichTextContentContainer(
    ) {
        super(
        );
        this.fxg_richtextcontents = new ArrayList<>();
    }

    public fxg_RichTextContentContainer(
        ArrayList<fxg_RichTextContent> fxg_richtextcontents    ) {
        this.fxg_richtextcontents = fxg_richtextcontents;
    }


    public List<fxg_RichTextContent> getFxg_richtextcontents() {
        return fxg_richtextcontents;
    }

    public void addFxg_richtextcontent(Fxg_richtextcontent fxg_richtextcontent) {
        this.fxg_richtextcontents.add(fxg_richtextcontent);
    }

}