





import java.util.List;
import java.util.ArrayList;

public class model_change_ModelChangePackage extends UnicaseModelElement {

    private int targetVersion;
    private int sourceVersion;



    public model_change_ModelChangePackage(
        int targetVersion,        int sourceVersion    ) {
        super(
        );
        this.targetVersion = targetVersion;
        this.sourceVersion = sourceVersion;
    }


    public int getTargetversion() {
        return targetVersion;
    }

    public void setTargetversion(int targetVersion) {
        this.targetVersion = targetVersion;
    }
    public int getSourceversion() {
        return sourceVersion;
    }

    public void setSourceversion(int sourceVersion) {
        this.sourceVersion = sourceVersion;
    }


}