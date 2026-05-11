





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_TextArea extends ComplexComponent {

    private String visibleLines;



    public metamodeloArquitecturaPila_TextArea(
        String visibleLines    ) {
        super(
        );
        this.visibleLines = visibleLines;
    }


    public String getVisiblelines() {
        return visibleLines;
    }

    public void setVisiblelines(String visibleLines) {
        this.visibleLines = visibleLines;
    }


}