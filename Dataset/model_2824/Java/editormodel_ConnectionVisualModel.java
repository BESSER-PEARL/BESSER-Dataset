





import java.util.List;
import java.util.ArrayList;

public class editormodel_ConnectionVisualModel extends NodeVisualModel {

    private String sourceTerminal;
    private String targetTerminal;



    public editormodel_ConnectionVisualModel(
        String sourceTerminal,        String targetTerminal    ) {
        super(
        );
        this.sourceTerminal = sourceTerminal;
        this.targetTerminal = targetTerminal;
    }


    public String getSourceterminal() {
        return sourceTerminal;
    }

    public void setSourceterminal(String sourceTerminal) {
        this.sourceTerminal = sourceTerminal;
    }
    public String getTargetterminal() {
        return targetTerminal;
    }

    public void setTargetterminal(String targetTerminal) {
        this.targetTerminal = targetTerminal;
    }


}