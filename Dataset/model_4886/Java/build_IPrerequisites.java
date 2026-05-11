





import java.util.List;
import java.util.ArrayList;

public class build_IPrerequisites extends IBuildPart {

    private String alias;
    private String rebasePath;



    public build_IPrerequisites(
        String alias,        String rebasePath    ) {
        super(
        );
        this.alias = alias;
        this.rebasePath = rebasePath;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getRebasepath() {
        return rebasePath;
    }

    public void setRebasepath(String rebasePath) {
        this.rebasePath = rebasePath;
    }


}