





import java.util.List;
import java.util.ArrayList;

public class PNML_AnnotationGraphics extends Graphics {






    private LabeledElement labeledelement;




    private Line line;




    private Fill fill;


    public PNML_AnnotationGraphics(
    ) {
        super(
        );
    }



    public LabeledElement getLabeledelement() {
        return labeledelement;
    }

    public void setLabeledelement(LabeledElement labeledelement) {
        this.labeledelement = labeledelement;
    }
    public Line getLine() {
        return line;
    }

    public void setLine(Line line) {
        this.line = line;
    }
    public Fill getFill() {
        return fill;
    }

    public void setFill(Fill fill) {
        this.fill = fill;
    }

}