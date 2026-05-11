





import java.util.List;
import java.util.ArrayList;

public class executionTrace_StoryPatternLinkExecution extends Execution {

    private String sourceObject;



    public executionTrace_StoryPatternLinkExecution(
        String sourceObject    ) {
        super(
        );
        this.sourceObject = sourceObject;
    }


    public String getSourceobject() {
        return sourceObject;
    }

    public void setSourceobject(String sourceObject) {
        this.sourceObject = sourceObject;
    }


}