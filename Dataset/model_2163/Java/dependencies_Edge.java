





import java.util.List;
import java.util.ArrayList;

public class dependencies_Edge  {

    private boolean referredTo;
    private boolean equal;





    private dependencies_Vertex dependencies_vertex;


    public dependencies_Edge(
        boolean referredTo,        boolean equal    ) {
        this.referredTo = referredTo;
        this.equal = equal;
    }


    public boolean getReferredto() {
        return referredTo;
    }

    public void setReferredto(boolean referredTo) {
        this.referredTo = referredTo;
    }
    public boolean getEqual() {
        return equal;
    }

    public void setEqual(boolean equal) {
        this.equal = equal;
    }

    public dependencies_Vertex getDependencies_vertex() {
        return dependencies_vertex;
    }

    public void setDependencies_vertex(dependencies_Vertex dependencies_vertex) {
        this.dependencies_vertex = dependencies_vertex;
    }

}