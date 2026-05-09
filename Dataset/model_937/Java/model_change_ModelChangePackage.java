





import java.util.List;
import java.util.ArrayList;

public class model_change_ModelChangePackage extends UnicaseModelElement {

    private int sourceVersion;
    private int targetVersion;



    public model_change_ModelChangePackage(
        int sourceVersion,        int targetVersion    ) {
        super(
        );
        this.sourceVersion = sourceVersion;
        this.targetVersion = targetVersion;
    }


    public int getSourceversion() {
        return sourceVersion;
    }

    public void setSourceversion(int sourceVersion) {
        this.sourceVersion = sourceVersion;
    }
    public int getTargetversion() {
        return targetVersion;
    }

    public void setTargetversion(int targetVersion) {
        this.targetVersion = targetVersion;
    }


}