





import java.util.List;
import java.util.ArrayList;

public class p2_ProfileDefinition extends ModelElement {

    private boolean includeSourceBundles;



    public p2_ProfileDefinition(
        boolean includeSourceBundles    ) {
        super(
        );
        this.includeSourceBundles = includeSourceBundles;
    }


    public boolean getIncludesourcebundles() {
        return includeSourceBundles;
    }

    public void setIncludesourcebundles(boolean includeSourceBundles) {
        this.includeSourceBundles = includeSourceBundles;
    }


}