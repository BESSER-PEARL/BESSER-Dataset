





import java.util.List;
import java.util.ArrayList;

public class positionmm_Counter extends NamedElement {

    private String script;
    private int position;



    public positionmm_Counter(
        String script,        int position    ) {
        super(
        );
        this.script = script;
        this.position = position;
    }


    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }


}