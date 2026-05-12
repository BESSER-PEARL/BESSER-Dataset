





import java.util.List;
import java.util.ArrayList;

public class maven_MavenProvider extends Provider {

    private boolean transitive;



    public maven_MavenProvider(
        boolean transitive    ) {
        super(
        );
        this.transitive = transitive;
    }


    public boolean getTransitive() {
        return transitive;
    }

    public void setTransitive(boolean transitive) {
        this.transitive = transitive;
    }


}