





import java.util.List;
import java.util.ArrayList;

public class notation_HintedDiagramLinkStyle extends Style, DiagramLinkStyle {

    private String hint;



    public notation_HintedDiagramLinkStyle(
        String hint    ) {
        super(
        );
        this.hint = hint;
    }


    public String getHint() {
        return hint;
    }

    public void setHint(String hint) {
        this.hint = hint;
    }


}